"""
88_88_insider_transaction_freq — Base Features 151-225
Domain: 88_insider_transaction_freq
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

def itf_151_rank_5d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 88 insider transaction freq to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = insider_buy_shares
    return _rank_pct(base, 5)

def itf_152_rank_21d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 88 insider transaction freq to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = insider_buy_shares
    return _rank_pct(base, 21)

def itf_153_rank_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 88 insider transaction freq to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = insider_buy_shares
    return _rank_pct(base, 63)

def itf_154_rank_126d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 88 insider transaction freq to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = insider_buy_shares
    return _rank_pct(base, 126)

def itf_155_rank_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 88 insider transaction freq to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = insider_buy_shares
    return _rank_pct(base, 252)

def itf_156_skew_5d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 88 insider transaction freq distribution over 5d to detect tail risk or exhaustion.
    """
    base = insider_buy_shares
    return _rolling_skew(base, 5)

def itf_157_skew_21d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 88 insider transaction freq distribution over 21d to detect tail risk or exhaustion.
    """
    base = insider_buy_shares
    return _rolling_skew(base, 21)

def itf_158_skew_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 88 insider transaction freq distribution over 63d to detect tail risk or exhaustion.
    """
    base = insider_buy_shares
    return _rolling_skew(base, 63)

def itf_159_skew_126d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 88 insider transaction freq distribution over 126d to detect tail risk or exhaustion.
    """
    base = insider_buy_shares
    return _rolling_skew(base, 126)

def itf_160_skew_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 88 insider transaction freq distribution over 252d to detect tail risk or exhaustion.
    """
    base = insider_buy_shares
    return _rolling_skew(base, 252)

def itf_161_kurt_5d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 88 insider transaction freq over 5d to capture explosive breakdown or reversal points.
    """
    base = insider_buy_shares
    return _rolling_kurt(base, 5)

def itf_162_kurt_21d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 88 insider transaction freq over 21d to capture explosive breakdown or reversal points.
    """
    base = insider_buy_shares
    return _rolling_kurt(base, 21)

def itf_163_kurt_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 88 insider transaction freq over 63d to capture explosive breakdown or reversal points.
    """
    base = insider_buy_shares
    return _rolling_kurt(base, 63)

def itf_164_kurt_126d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 88 insider transaction freq over 126d to capture explosive breakdown or reversal points.
    """
    base = insider_buy_shares
    return _rolling_kurt(base, 126)

def itf_165_kurt_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 88 insider transaction freq over 252d to capture explosive breakdown or reversal points.
    """
    base = insider_buy_shares
    return _rolling_kurt(base, 252)

def itf_166_voladj_5d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 88 insider transaction freq for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = insider_buy_shares
    return _safe_div(base, _rolling_std(base, 5))

def itf_167_voladj_21d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 88 insider transaction freq for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = insider_buy_shares
    return _safe_div(base, _rolling_std(base, 21))

def itf_168_voladj_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 88 insider transaction freq for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = insider_buy_shares
    return _safe_div(base, _rolling_std(base, 63))

def itf_169_voladj_126d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 88 insider transaction freq for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = insider_buy_shares
    return _safe_div(base, _rolling_std(base, 126))

def itf_170_voladj_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 88 insider transaction freq for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = insider_buy_shares
    return _safe_div(base, _rolling_std(base, 252))

def itf_171_lognorm_5d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 88 insider transaction freq over 5d to stabilize variance and capture exponential shifts.
    """
    base = insider_buy_shares
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def itf_172_lognorm_21d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 88 insider transaction freq over 21d to stabilize variance and capture exponential shifts.
    """
    base = insider_buy_shares
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def itf_173_lognorm_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 88 insider transaction freq over 63d to stabilize variance and capture exponential shifts.
    """
    base = insider_buy_shares
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def itf_174_lognorm_126d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 88 insider transaction freq over 126d to stabilize variance and capture exponential shifts.
    """
    base = insider_buy_shares
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def itf_175_lognorm_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 88 insider transaction freq over 252d to stabilize variance and capture exponential shifts.
    """
    base = insider_buy_shares
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def itf_176_lvl_5d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 88 insider transaction freq over a 5d horizon to identify extreme regimes.
    """
    base = officer_buy_value
    return _rolling_mean(base, 5)

def itf_177_lvl_21d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 88 insider transaction freq over a 21d horizon to identify extreme regimes.
    """
    base = officer_buy_value
    return _rolling_mean(base, 21)

def itf_178_lvl_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 88 insider transaction freq over a 63d horizon to identify extreme regimes.
    """
    base = officer_buy_value
    return _rolling_mean(base, 63)

def itf_179_lvl_126d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 88 insider transaction freq over a 126d horizon to identify extreme regimes.
    """
    base = officer_buy_value
    return _rolling_mean(base, 126)

def itf_180_lvl_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 88 insider transaction freq over a 252d horizon to identify extreme regimes.
    """
    base = officer_buy_value
    return _rolling_mean(base, 252)

def itf_181_zscore_5d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 88 insider transaction freq by measuring deviations from the 5d mean.
    """
    base = officer_buy_value
    return _zscore_rolling(base, 5)

def itf_182_zscore_21d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 88 insider transaction freq by measuring deviations from the 21d mean.
    """
    base = officer_buy_value
    return _zscore_rolling(base, 21)

def itf_183_zscore_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 88 insider transaction freq by measuring deviations from the 63d mean.
    """
    base = officer_buy_value
    return _zscore_rolling(base, 63)

def itf_184_zscore_126d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 88 insider transaction freq by measuring deviations from the 126d mean.
    """
    base = officer_buy_value
    return _zscore_rolling(base, 126)

def itf_185_zscore_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 88 insider transaction freq by measuring deviations from the 252d mean.
    """
    base = officer_buy_value
    return _zscore_rolling(base, 252)

def itf_186_rank_5d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 88 insider transaction freq to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = officer_buy_value
    return _rank_pct(base, 5)

def itf_187_rank_21d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 88 insider transaction freq to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = officer_buy_value
    return _rank_pct(base, 21)

def itf_188_rank_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 88 insider transaction freq to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = officer_buy_value
    return _rank_pct(base, 63)

def itf_189_rank_126d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 88 insider transaction freq to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = officer_buy_value
    return _rank_pct(base, 126)

def itf_190_rank_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 88 insider transaction freq to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = officer_buy_value
    return _rank_pct(base, 252)

def itf_191_skew_5d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 88 insider transaction freq distribution over 5d to detect tail risk or exhaustion.
    """
    base = officer_buy_value
    return _rolling_skew(base, 5)

def itf_192_skew_21d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 88 insider transaction freq distribution over 21d to detect tail risk or exhaustion.
    """
    base = officer_buy_value
    return _rolling_skew(base, 21)

def itf_193_skew_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 88 insider transaction freq distribution over 63d to detect tail risk or exhaustion.
    """
    base = officer_buy_value
    return _rolling_skew(base, 63)

def itf_194_skew_126d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 88 insider transaction freq distribution over 126d to detect tail risk or exhaustion.
    """
    base = officer_buy_value
    return _rolling_skew(base, 126)

def itf_195_skew_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 88 insider transaction freq distribution over 252d to detect tail risk or exhaustion.
    """
    base = officer_buy_value
    return _rolling_skew(base, 252)

def itf_196_kurt_5d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 88 insider transaction freq over 5d to capture explosive breakdown or reversal points.
    """
    base = officer_buy_value
    return _rolling_kurt(base, 5)

def itf_197_kurt_21d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 88 insider transaction freq over 21d to capture explosive breakdown or reversal points.
    """
    base = officer_buy_value
    return _rolling_kurt(base, 21)

def itf_198_kurt_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 88 insider transaction freq over 63d to capture explosive breakdown or reversal points.
    """
    base = officer_buy_value
    return _rolling_kurt(base, 63)

def itf_199_kurt_126d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 88 insider transaction freq over 126d to capture explosive breakdown or reversal points.
    """
    base = officer_buy_value
    return _rolling_kurt(base, 126)

def itf_200_kurt_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 88 insider transaction freq over 252d to capture explosive breakdown or reversal points.
    """
    base = officer_buy_value
    return _rolling_kurt(base, 252)

def itf_201_voladj_5d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 88 insider transaction freq for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = officer_buy_value
    return _safe_div(base, _rolling_std(base, 5))

def itf_202_voladj_21d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 88 insider transaction freq for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = officer_buy_value
    return _safe_div(base, _rolling_std(base, 21))

def itf_203_voladj_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 88 insider transaction freq for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = officer_buy_value
    return _safe_div(base, _rolling_std(base, 63))

def itf_204_voladj_126d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 88 insider transaction freq for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = officer_buy_value
    return _safe_div(base, _rolling_std(base, 126))

def itf_205_voladj_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 88 insider transaction freq for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = officer_buy_value
    return _safe_div(base, _rolling_std(base, 252))

def itf_206_lognorm_5d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 88 insider transaction freq over 5d to stabilize variance and capture exponential shifts.
    """
    base = officer_buy_value
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def itf_207_lognorm_21d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 88 insider transaction freq over 21d to stabilize variance and capture exponential shifts.
    """
    base = officer_buy_value
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def itf_208_lognorm_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 88 insider transaction freq over 63d to stabilize variance and capture exponential shifts.
    """
    base = officer_buy_value
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def itf_209_lognorm_126d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 88 insider transaction freq over 126d to stabilize variance and capture exponential shifts.
    """
    base = officer_buy_value
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def itf_210_lognorm_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 88 insider transaction freq over 252d to stabilize variance and capture exponential shifts.
    """
    base = officer_buy_value
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def itf_211_lvl_5d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 88 insider transaction freq over a 5d horizon to identify extreme regimes.
    """
    base = director_buy_value
    return _rolling_mean(base, 5)

def itf_212_lvl_21d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 88 insider transaction freq over a 21d horizon to identify extreme regimes.
    """
    base = director_buy_value
    return _rolling_mean(base, 21)

def itf_213_lvl_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 88 insider transaction freq over a 63d horizon to identify extreme regimes.
    """
    base = director_buy_value
    return _rolling_mean(base, 63)

def itf_214_lvl_126d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 88 insider transaction freq over a 126d horizon to identify extreme regimes.
    """
    base = director_buy_value
    return _rolling_mean(base, 126)

def itf_215_lvl_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 88 insider transaction freq over a 252d horizon to identify extreme regimes.
    """
    base = director_buy_value
    return _rolling_mean(base, 252)

def itf_216_zscore_5d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 88 insider transaction freq by measuring deviations from the 5d mean.
    """
    base = director_buy_value
    return _zscore_rolling(base, 5)

def itf_217_zscore_21d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 88 insider transaction freq by measuring deviations from the 21d mean.
    """
    base = director_buy_value
    return _zscore_rolling(base, 21)

def itf_218_zscore_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 88 insider transaction freq by measuring deviations from the 63d mean.
    """
    base = director_buy_value
    return _zscore_rolling(base, 63)

def itf_219_zscore_126d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 88 insider transaction freq by measuring deviations from the 126d mean.
    """
    base = director_buy_value
    return _zscore_rolling(base, 126)

def itf_220_zscore_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 88 insider transaction freq by measuring deviations from the 252d mean.
    """
    base = director_buy_value
    return _zscore_rolling(base, 252)

def itf_221_rank_5d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 88 insider transaction freq to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = director_buy_value
    return _rank_pct(base, 5)

def itf_222_rank_21d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 88 insider transaction freq to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = director_buy_value
    return _rank_pct(base, 21)

def itf_223_rank_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 88 insider transaction freq to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = director_buy_value
    return _rank_pct(base, 63)

def itf_224_rank_126d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 88 insider transaction freq to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = director_buy_value
    return _rank_pct(base, 126)

def itf_225_rank_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 88 insider transaction freq to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = director_buy_value
    return _rank_pct(base, 252)
