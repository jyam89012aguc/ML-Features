"""
37_37_range_expansion — Base Features 151-225
Domain: 37_range_expansion
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

def rexp_151_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 37 range expansion to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = (close.pct_change(5).rolling(25).mean())
    return _rank_pct(base, 5)

def rexp_152_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 37 range expansion to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = (close.pct_change(5).rolling(25).mean())
    return _rank_pct(base, 21)

def rexp_153_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 37 range expansion to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = (close.pct_change(5).rolling(25).mean())
    return _rank_pct(base, 63)

def rexp_154_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 37 range expansion to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = (close.pct_change(5).rolling(25).mean())
    return _rank_pct(base, 126)

def rexp_155_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 37 range expansion to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = (close.pct_change(5).rolling(25).mean())
    return _rank_pct(base, 252)

def rexp_156_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 37 range expansion distribution over 5d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(5).rolling(25).mean())
    return _rolling_skew(base, 5)

def rexp_157_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 37 range expansion distribution over 21d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(5).rolling(25).mean())
    return _rolling_skew(base, 21)

def rexp_158_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 37 range expansion distribution over 63d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(5).rolling(25).mean())
    return _rolling_skew(base, 63)

def rexp_159_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 37 range expansion distribution over 126d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(5).rolling(25).mean())
    return _rolling_skew(base, 126)

def rexp_160_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 37 range expansion distribution over 252d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(5).rolling(25).mean())
    return _rolling_skew(base, 252)

def rexp_161_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 37 range expansion over 5d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(5).rolling(25).mean())
    return _rolling_kurt(base, 5)

def rexp_162_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 37 range expansion over 21d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(5).rolling(25).mean())
    return _rolling_kurt(base, 21)

def rexp_163_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 37 range expansion over 63d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(5).rolling(25).mean())
    return _rolling_kurt(base, 63)

def rexp_164_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 37 range expansion over 126d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(5).rolling(25).mean())
    return _rolling_kurt(base, 126)

def rexp_165_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 37 range expansion over 252d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(5).rolling(25).mean())
    return _rolling_kurt(base, 252)

def rexp_166_voladj_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 37 range expansion for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(5).rolling(25).mean())
    return _safe_div(base, _rolling_std(base, 5))

def rexp_167_voladj_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 37 range expansion for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(5).rolling(25).mean())
    return _safe_div(base, _rolling_std(base, 21))

def rexp_168_voladj_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 37 range expansion for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(5).rolling(25).mean())
    return _safe_div(base, _rolling_std(base, 63))

def rexp_169_voladj_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 37 range expansion for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(5).rolling(25).mean())
    return _safe_div(base, _rolling_std(base, 126))

def rexp_170_voladj_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 37 range expansion for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(5).rolling(25).mean())
    return _safe_div(base, _rolling_std(base, 252))

def rexp_171_lognorm_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 37 range expansion over 5d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(5).rolling(25).mean())
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def rexp_172_lognorm_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 37 range expansion over 21d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(5).rolling(25).mean())
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def rexp_173_lognorm_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 37 range expansion over 63d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(5).rolling(25).mean())
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def rexp_174_lognorm_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 37 range expansion over 126d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(5).rolling(25).mean())
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def rexp_175_lognorm_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 37 range expansion over 252d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(5).rolling(25).mean())
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def rexp_176_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 37 range expansion over a 5d horizon to identify extreme regimes.
    """
    base = (close.pct_change(6).rolling(30).mean())
    return _rolling_mean(base, 5)

def rexp_177_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 37 range expansion over a 21d horizon to identify extreme regimes.
    """
    base = (close.pct_change(6).rolling(30).mean())
    return _rolling_mean(base, 21)

def rexp_178_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 37 range expansion over a 63d horizon to identify extreme regimes.
    """
    base = (close.pct_change(6).rolling(30).mean())
    return _rolling_mean(base, 63)

def rexp_179_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 37 range expansion over a 126d horizon to identify extreme regimes.
    """
    base = (close.pct_change(6).rolling(30).mean())
    return _rolling_mean(base, 126)

def rexp_180_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 37 range expansion over a 252d horizon to identify extreme regimes.
    """
    base = (close.pct_change(6).rolling(30).mean())
    return _rolling_mean(base, 252)

def rexp_181_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 37 range expansion by measuring deviations from the 5d mean.
    """
    base = (close.pct_change(6).rolling(30).mean())
    return _zscore_rolling(base, 5)

def rexp_182_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 37 range expansion by measuring deviations from the 21d mean.
    """
    base = (close.pct_change(6).rolling(30).mean())
    return _zscore_rolling(base, 21)

def rexp_183_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 37 range expansion by measuring deviations from the 63d mean.
    """
    base = (close.pct_change(6).rolling(30).mean())
    return _zscore_rolling(base, 63)

def rexp_184_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 37 range expansion by measuring deviations from the 126d mean.
    """
    base = (close.pct_change(6).rolling(30).mean())
    return _zscore_rolling(base, 126)

def rexp_185_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 37 range expansion by measuring deviations from the 252d mean.
    """
    base = (close.pct_change(6).rolling(30).mean())
    return _zscore_rolling(base, 252)

def rexp_186_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 37 range expansion to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = (close.pct_change(6).rolling(30).mean())
    return _rank_pct(base, 5)

def rexp_187_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 37 range expansion to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = (close.pct_change(6).rolling(30).mean())
    return _rank_pct(base, 21)

def rexp_188_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 37 range expansion to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = (close.pct_change(6).rolling(30).mean())
    return _rank_pct(base, 63)

def rexp_189_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 37 range expansion to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = (close.pct_change(6).rolling(30).mean())
    return _rank_pct(base, 126)

def rexp_190_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 37 range expansion to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = (close.pct_change(6).rolling(30).mean())
    return _rank_pct(base, 252)

def rexp_191_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 37 range expansion distribution over 5d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(6).rolling(30).mean())
    return _rolling_skew(base, 5)

def rexp_192_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 37 range expansion distribution over 21d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(6).rolling(30).mean())
    return _rolling_skew(base, 21)

def rexp_193_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 37 range expansion distribution over 63d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(6).rolling(30).mean())
    return _rolling_skew(base, 63)

def rexp_194_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 37 range expansion distribution over 126d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(6).rolling(30).mean())
    return _rolling_skew(base, 126)

def rexp_195_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 37 range expansion distribution over 252d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(6).rolling(30).mean())
    return _rolling_skew(base, 252)

def rexp_196_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 37 range expansion over 5d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(6).rolling(30).mean())
    return _rolling_kurt(base, 5)

def rexp_197_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 37 range expansion over 21d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(6).rolling(30).mean())
    return _rolling_kurt(base, 21)

def rexp_198_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 37 range expansion over 63d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(6).rolling(30).mean())
    return _rolling_kurt(base, 63)

def rexp_199_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 37 range expansion over 126d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(6).rolling(30).mean())
    return _rolling_kurt(base, 126)

def rexp_200_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 37 range expansion over 252d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(6).rolling(30).mean())
    return _rolling_kurt(base, 252)

def rexp_201_voladj_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 37 range expansion for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(6).rolling(30).mean())
    return _safe_div(base, _rolling_std(base, 5))

def rexp_202_voladj_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 37 range expansion for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(6).rolling(30).mean())
    return _safe_div(base, _rolling_std(base, 21))

def rexp_203_voladj_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 37 range expansion for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(6).rolling(30).mean())
    return _safe_div(base, _rolling_std(base, 63))

def rexp_204_voladj_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 37 range expansion for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(6).rolling(30).mean())
    return _safe_div(base, _rolling_std(base, 126))

def rexp_205_voladj_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 37 range expansion for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(6).rolling(30).mean())
    return _safe_div(base, _rolling_std(base, 252))

def rexp_206_lognorm_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 37 range expansion over 5d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(6).rolling(30).mean())
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def rexp_207_lognorm_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 37 range expansion over 21d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(6).rolling(30).mean())
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def rexp_208_lognorm_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 37 range expansion over 63d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(6).rolling(30).mean())
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def rexp_209_lognorm_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 37 range expansion over 126d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(6).rolling(30).mean())
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def rexp_210_lognorm_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 37 range expansion over 252d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(6).rolling(30).mean())
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def rexp_211_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 37 range expansion over a 5d horizon to identify extreme regimes.
    """
    base = (close.pct_change(7).rolling(35).mean())
    return _rolling_mean(base, 5)

def rexp_212_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 37 range expansion over a 21d horizon to identify extreme regimes.
    """
    base = (close.pct_change(7).rolling(35).mean())
    return _rolling_mean(base, 21)

def rexp_213_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 37 range expansion over a 63d horizon to identify extreme regimes.
    """
    base = (close.pct_change(7).rolling(35).mean())
    return _rolling_mean(base, 63)

def rexp_214_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 37 range expansion over a 126d horizon to identify extreme regimes.
    """
    base = (close.pct_change(7).rolling(35).mean())
    return _rolling_mean(base, 126)

def rexp_215_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 37 range expansion over a 252d horizon to identify extreme regimes.
    """
    base = (close.pct_change(7).rolling(35).mean())
    return _rolling_mean(base, 252)

def rexp_216_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 37 range expansion by measuring deviations from the 5d mean.
    """
    base = (close.pct_change(7).rolling(35).mean())
    return _zscore_rolling(base, 5)

def rexp_217_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 37 range expansion by measuring deviations from the 21d mean.
    """
    base = (close.pct_change(7).rolling(35).mean())
    return _zscore_rolling(base, 21)

def rexp_218_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 37 range expansion by measuring deviations from the 63d mean.
    """
    base = (close.pct_change(7).rolling(35).mean())
    return _zscore_rolling(base, 63)

def rexp_219_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 37 range expansion by measuring deviations from the 126d mean.
    """
    base = (close.pct_change(7).rolling(35).mean())
    return _zscore_rolling(base, 126)

def rexp_220_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 37 range expansion by measuring deviations from the 252d mean.
    """
    base = (close.pct_change(7).rolling(35).mean())
    return _zscore_rolling(base, 252)

def rexp_221_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 37 range expansion to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = (close.pct_change(7).rolling(35).mean())
    return _rank_pct(base, 5)

def rexp_222_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 37 range expansion to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = (close.pct_change(7).rolling(35).mean())
    return _rank_pct(base, 21)

def rexp_223_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 37 range expansion to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = (close.pct_change(7).rolling(35).mean())
    return _rank_pct(base, 63)

def rexp_224_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 37 range expansion to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = (close.pct_change(7).rolling(35).mean())
    return _rank_pct(base, 126)

def rexp_225_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 37 range expansion to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = (close.pct_change(7).rolling(35).mean())
    return _rank_pct(base, 252)
