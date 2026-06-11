"""
95_95_forced_selling_proxy — Base Features 151-225
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

def fsel_151_rank_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 95 forced selling proxy to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = inst_shares_held
    return _rank_pct(base, 5)

def fsel_152_rank_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 95 forced selling proxy to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = inst_shares_held
    return _rank_pct(base, 21)

def fsel_153_rank_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 95 forced selling proxy to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = inst_shares_held
    return _rank_pct(base, 63)

def fsel_154_rank_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 95 forced selling proxy to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = inst_shares_held
    return _rank_pct(base, 126)

def fsel_155_rank_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 95 forced selling proxy to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = inst_shares_held
    return _rank_pct(base, 252)

def fsel_156_skew_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 95 forced selling proxy distribution over 5d to detect tail risk or exhaustion.
    """
    base = inst_shares_held
    return _rolling_skew(base, 5)

def fsel_157_skew_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 95 forced selling proxy distribution over 21d to detect tail risk or exhaustion.
    """
    base = inst_shares_held
    return _rolling_skew(base, 21)

def fsel_158_skew_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 95 forced selling proxy distribution over 63d to detect tail risk or exhaustion.
    """
    base = inst_shares_held
    return _rolling_skew(base, 63)

def fsel_159_skew_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 95 forced selling proxy distribution over 126d to detect tail risk or exhaustion.
    """
    base = inst_shares_held
    return _rolling_skew(base, 126)

def fsel_160_skew_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 95 forced selling proxy distribution over 252d to detect tail risk or exhaustion.
    """
    base = inst_shares_held
    return _rolling_skew(base, 252)

def fsel_161_kurt_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 95 forced selling proxy over 5d to capture explosive breakdown or reversal points.
    """
    base = inst_shares_held
    return _rolling_kurt(base, 5)

def fsel_162_kurt_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 95 forced selling proxy over 21d to capture explosive breakdown or reversal points.
    """
    base = inst_shares_held
    return _rolling_kurt(base, 21)

def fsel_163_kurt_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 95 forced selling proxy over 63d to capture explosive breakdown or reversal points.
    """
    base = inst_shares_held
    return _rolling_kurt(base, 63)

def fsel_164_kurt_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 95 forced selling proxy over 126d to capture explosive breakdown or reversal points.
    """
    base = inst_shares_held
    return _rolling_kurt(base, 126)

def fsel_165_kurt_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 95 forced selling proxy over 252d to capture explosive breakdown or reversal points.
    """
    base = inst_shares_held
    return _rolling_kurt(base, 252)

def fsel_166_voladj_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 95 forced selling proxy for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = inst_shares_held
    return _safe_div(base, _rolling_std(base, 5))

def fsel_167_voladj_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 95 forced selling proxy for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = inst_shares_held
    return _safe_div(base, _rolling_std(base, 21))

def fsel_168_voladj_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 95 forced selling proxy for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = inst_shares_held
    return _safe_div(base, _rolling_std(base, 63))

def fsel_169_voladj_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 95 forced selling proxy for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = inst_shares_held
    return _safe_div(base, _rolling_std(base, 126))

def fsel_170_voladj_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 95 forced selling proxy for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = inst_shares_held
    return _safe_div(base, _rolling_std(base, 252))

def fsel_171_lognorm_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 95 forced selling proxy over 5d to stabilize variance and capture exponential shifts.
    """
    base = inst_shares_held
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def fsel_172_lognorm_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 95 forced selling proxy over 21d to stabilize variance and capture exponential shifts.
    """
    base = inst_shares_held
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def fsel_173_lognorm_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 95 forced selling proxy over 63d to stabilize variance and capture exponential shifts.
    """
    base = inst_shares_held
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def fsel_174_lognorm_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 95 forced selling proxy over 126d to stabilize variance and capture exponential shifts.
    """
    base = inst_shares_held
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def fsel_175_lognorm_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 95 forced selling proxy over 252d to stabilize variance and capture exponential shifts.
    """
    base = inst_shares_held
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def fsel_176_lvl_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 95 forced selling proxy over a 5d horizon to identify extreme regimes.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return _rolling_mean(base, 5)

def fsel_177_lvl_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 95 forced selling proxy over a 21d horizon to identify extreme regimes.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return _rolling_mean(base, 21)

def fsel_178_lvl_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 95 forced selling proxy over a 63d horizon to identify extreme regimes.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return _rolling_mean(base, 63)

def fsel_179_lvl_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 95 forced selling proxy over a 126d horizon to identify extreme regimes.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return _rolling_mean(base, 126)

def fsel_180_lvl_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 95 forced selling proxy over a 252d horizon to identify extreme regimes.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return _rolling_mean(base, 252)

def fsel_181_zscore_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 95 forced selling proxy by measuring deviations from the 5d mean.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return _zscore_rolling(base, 5)

def fsel_182_zscore_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 95 forced selling proxy by measuring deviations from the 21d mean.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return _zscore_rolling(base, 21)

def fsel_183_zscore_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 95 forced selling proxy by measuring deviations from the 63d mean.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return _zscore_rolling(base, 63)

def fsel_184_zscore_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 95 forced selling proxy by measuring deviations from the 126d mean.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return _zscore_rolling(base, 126)

def fsel_185_zscore_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 95 forced selling proxy by measuring deviations from the 252d mean.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return _zscore_rolling(base, 252)

def fsel_186_rank_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 95 forced selling proxy to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return _rank_pct(base, 5)

def fsel_187_rank_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 95 forced selling proxy to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return _rank_pct(base, 21)

def fsel_188_rank_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 95 forced selling proxy to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return _rank_pct(base, 63)

def fsel_189_rank_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 95 forced selling proxy to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return _rank_pct(base, 126)

def fsel_190_rank_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 95 forced selling proxy to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return _rank_pct(base, 252)

def fsel_191_skew_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 95 forced selling proxy distribution over 5d to detect tail risk or exhaustion.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return _rolling_skew(base, 5)

def fsel_192_skew_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 95 forced selling proxy distribution over 21d to detect tail risk or exhaustion.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return _rolling_skew(base, 21)

def fsel_193_skew_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 95 forced selling proxy distribution over 63d to detect tail risk or exhaustion.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return _rolling_skew(base, 63)

def fsel_194_skew_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 95 forced selling proxy distribution over 126d to detect tail risk or exhaustion.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return _rolling_skew(base, 126)

def fsel_195_skew_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 95 forced selling proxy distribution over 252d to detect tail risk or exhaustion.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return _rolling_skew(base, 252)

def fsel_196_kurt_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 95 forced selling proxy over 5d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return _rolling_kurt(base, 5)

def fsel_197_kurt_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 95 forced selling proxy over 21d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return _rolling_kurt(base, 21)

def fsel_198_kurt_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 95 forced selling proxy over 63d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return _rolling_kurt(base, 63)

def fsel_199_kurt_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 95 forced selling proxy over 126d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return _rolling_kurt(base, 126)

def fsel_200_kurt_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 95 forced selling proxy over 252d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return _rolling_kurt(base, 252)

def fsel_201_voladj_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 95 forced selling proxy for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return _safe_div(base, _rolling_std(base, 5))

def fsel_202_voladj_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 95 forced selling proxy for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return _safe_div(base, _rolling_std(base, 21))

def fsel_203_voladj_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 95 forced selling proxy for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return _safe_div(base, _rolling_std(base, 63))

def fsel_204_voladj_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 95 forced selling proxy for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return _safe_div(base, _rolling_std(base, 126))

def fsel_205_voladj_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 95 forced selling proxy for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return _safe_div(base, _rolling_std(base, 252))

def fsel_206_lognorm_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 95 forced selling proxy over 5d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def fsel_207_lognorm_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 95 forced selling proxy over 21d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def fsel_208_lognorm_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 95 forced selling proxy over 63d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def fsel_209_lognorm_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 95 forced selling proxy over 126d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def fsel_210_lognorm_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 95 forced selling proxy over 252d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(inst_buy_value, inst_buy_value + inst_sell_value)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def fsel_211_lvl_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 95 forced selling proxy over a 5d horizon to identify extreme regimes.
    """
    base = _safe_div(inst_sell_value, inst_shares_held)
    return _rolling_mean(base, 5)

def fsel_212_lvl_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 95 forced selling proxy over a 21d horizon to identify extreme regimes.
    """
    base = _safe_div(inst_sell_value, inst_shares_held)
    return _rolling_mean(base, 21)

def fsel_213_lvl_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 95 forced selling proxy over a 63d horizon to identify extreme regimes.
    """
    base = _safe_div(inst_sell_value, inst_shares_held)
    return _rolling_mean(base, 63)

def fsel_214_lvl_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 95 forced selling proxy over a 126d horizon to identify extreme regimes.
    """
    base = _safe_div(inst_sell_value, inst_shares_held)
    return _rolling_mean(base, 126)

def fsel_215_lvl_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 95 forced selling proxy over a 252d horizon to identify extreme regimes.
    """
    base = _safe_div(inst_sell_value, inst_shares_held)
    return _rolling_mean(base, 252)

def fsel_216_zscore_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 95 forced selling proxy by measuring deviations from the 5d mean.
    """
    base = _safe_div(inst_sell_value, inst_shares_held)
    return _zscore_rolling(base, 5)

def fsel_217_zscore_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 95 forced selling proxy by measuring deviations from the 21d mean.
    """
    base = _safe_div(inst_sell_value, inst_shares_held)
    return _zscore_rolling(base, 21)

def fsel_218_zscore_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 95 forced selling proxy by measuring deviations from the 63d mean.
    """
    base = _safe_div(inst_sell_value, inst_shares_held)
    return _zscore_rolling(base, 63)

def fsel_219_zscore_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 95 forced selling proxy by measuring deviations from the 126d mean.
    """
    base = _safe_div(inst_sell_value, inst_shares_held)
    return _zscore_rolling(base, 126)

def fsel_220_zscore_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 95 forced selling proxy by measuring deviations from the 252d mean.
    """
    base = _safe_div(inst_sell_value, inst_shares_held)
    return _zscore_rolling(base, 252)

def fsel_221_rank_5d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 95 forced selling proxy to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = _safe_div(inst_sell_value, inst_shares_held)
    return _rank_pct(base, 5)

def fsel_222_rank_21d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 95 forced selling proxy to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = _safe_div(inst_sell_value, inst_shares_held)
    return _rank_pct(base, 21)

def fsel_223_rank_63d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 95 forced selling proxy to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = _safe_div(inst_sell_value, inst_shares_held)
    return _rank_pct(base, 63)

def fsel_224_rank_126d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 95 forced selling proxy to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = _safe_div(inst_sell_value, inst_shares_held)
    return _rank_pct(base, 126)

def fsel_225_rank_252d(inst_buy_value: pd.Series, inst_sell_value: pd.Series, holder_count: pd.Series, inst_shares_held: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 95 forced selling proxy to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = _safe_div(inst_sell_value, inst_shares_held)
    return _rank_pct(base, 252)
