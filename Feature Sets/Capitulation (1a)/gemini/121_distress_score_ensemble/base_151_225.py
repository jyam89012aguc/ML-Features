"""
121_121_distress_score_ensemble — Base Features 151-225
Domain: 121_distress_score_ensemble
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

def dsen_151_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 121 distress score ensemble to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = (_zscore_rolling(close, 50) + _zscore_rolling(volume, 50)) / 2
    return _rank_pct(base, 5)

def dsen_152_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 121 distress score ensemble to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = (_zscore_rolling(close, 50) + _zscore_rolling(volume, 50)) / 2
    return _rank_pct(base, 21)

def dsen_153_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 121 distress score ensemble to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = (_zscore_rolling(close, 50) + _zscore_rolling(volume, 50)) / 2
    return _rank_pct(base, 63)

def dsen_154_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 121 distress score ensemble to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = (_zscore_rolling(close, 50) + _zscore_rolling(volume, 50)) / 2
    return _rank_pct(base, 126)

def dsen_155_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 121 distress score ensemble to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = (_zscore_rolling(close, 50) + _zscore_rolling(volume, 50)) / 2
    return _rank_pct(base, 252)

def dsen_156_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 121 distress score ensemble distribution over 5d to detect tail risk or exhaustion.
    """
    base = (_zscore_rolling(close, 50) + _zscore_rolling(volume, 50)) / 2
    return _rolling_skew(base, 5)

def dsen_157_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 121 distress score ensemble distribution over 21d to detect tail risk or exhaustion.
    """
    base = (_zscore_rolling(close, 50) + _zscore_rolling(volume, 50)) / 2
    return _rolling_skew(base, 21)

def dsen_158_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 121 distress score ensemble distribution over 63d to detect tail risk or exhaustion.
    """
    base = (_zscore_rolling(close, 50) + _zscore_rolling(volume, 50)) / 2
    return _rolling_skew(base, 63)

def dsen_159_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 121 distress score ensemble distribution over 126d to detect tail risk or exhaustion.
    """
    base = (_zscore_rolling(close, 50) + _zscore_rolling(volume, 50)) / 2
    return _rolling_skew(base, 126)

def dsen_160_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 121 distress score ensemble distribution over 252d to detect tail risk or exhaustion.
    """
    base = (_zscore_rolling(close, 50) + _zscore_rolling(volume, 50)) / 2
    return _rolling_skew(base, 252)

def dsen_161_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 121 distress score ensemble over 5d to capture explosive breakdown or reversal points.
    """
    base = (_zscore_rolling(close, 50) + _zscore_rolling(volume, 50)) / 2
    return _rolling_kurt(base, 5)

def dsen_162_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 121 distress score ensemble over 21d to capture explosive breakdown or reversal points.
    """
    base = (_zscore_rolling(close, 50) + _zscore_rolling(volume, 50)) / 2
    return _rolling_kurt(base, 21)

def dsen_163_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 121 distress score ensemble over 63d to capture explosive breakdown or reversal points.
    """
    base = (_zscore_rolling(close, 50) + _zscore_rolling(volume, 50)) / 2
    return _rolling_kurt(base, 63)

def dsen_164_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 121 distress score ensemble over 126d to capture explosive breakdown or reversal points.
    """
    base = (_zscore_rolling(close, 50) + _zscore_rolling(volume, 50)) / 2
    return _rolling_kurt(base, 126)

def dsen_165_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 121 distress score ensemble over 252d to capture explosive breakdown or reversal points.
    """
    base = (_zscore_rolling(close, 50) + _zscore_rolling(volume, 50)) / 2
    return _rolling_kurt(base, 252)

def dsen_166_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 121 distress score ensemble for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = (_zscore_rolling(close, 50) + _zscore_rolling(volume, 50)) / 2
    return _safe_div(base, _rolling_std(base, 5))

def dsen_167_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 121 distress score ensemble for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = (_zscore_rolling(close, 50) + _zscore_rolling(volume, 50)) / 2
    return _safe_div(base, _rolling_std(base, 21))

def dsen_168_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 121 distress score ensemble for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = (_zscore_rolling(close, 50) + _zscore_rolling(volume, 50)) / 2
    return _safe_div(base, _rolling_std(base, 63))

def dsen_169_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 121 distress score ensemble for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = (_zscore_rolling(close, 50) + _zscore_rolling(volume, 50)) / 2
    return _safe_div(base, _rolling_std(base, 126))

def dsen_170_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 121 distress score ensemble for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = (_zscore_rolling(close, 50) + _zscore_rolling(volume, 50)) / 2
    return _safe_div(base, _rolling_std(base, 252))

def dsen_171_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 121 distress score ensemble over 5d to stabilize variance and capture exponential shifts.
    """
    base = (_zscore_rolling(close, 50) + _zscore_rolling(volume, 50)) / 2
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def dsen_172_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 121 distress score ensemble over 21d to stabilize variance and capture exponential shifts.
    """
    base = (_zscore_rolling(close, 50) + _zscore_rolling(volume, 50)) / 2
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def dsen_173_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 121 distress score ensemble over 63d to stabilize variance and capture exponential shifts.
    """
    base = (_zscore_rolling(close, 50) + _zscore_rolling(volume, 50)) / 2
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def dsen_174_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 121 distress score ensemble over 126d to stabilize variance and capture exponential shifts.
    """
    base = (_zscore_rolling(close, 50) + _zscore_rolling(volume, 50)) / 2
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def dsen_175_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 121 distress score ensemble over 252d to stabilize variance and capture exponential shifts.
    """
    base = (_zscore_rolling(close, 50) + _zscore_rolling(volume, 50)) / 2
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def dsen_176_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 121 distress score ensemble over a 5d horizon to identify extreme regimes.
    """
    base = (_zscore_rolling(close, 60) + _zscore_rolling(volume, 60)) / 2
    return _rolling_mean(base, 5)

def dsen_177_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 121 distress score ensemble over a 21d horizon to identify extreme regimes.
    """
    base = (_zscore_rolling(close, 60) + _zscore_rolling(volume, 60)) / 2
    return _rolling_mean(base, 21)

def dsen_178_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 121 distress score ensemble over a 63d horizon to identify extreme regimes.
    """
    base = (_zscore_rolling(close, 60) + _zscore_rolling(volume, 60)) / 2
    return _rolling_mean(base, 63)

def dsen_179_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 121 distress score ensemble over a 126d horizon to identify extreme regimes.
    """
    base = (_zscore_rolling(close, 60) + _zscore_rolling(volume, 60)) / 2
    return _rolling_mean(base, 126)

def dsen_180_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 121 distress score ensemble over a 252d horizon to identify extreme regimes.
    """
    base = (_zscore_rolling(close, 60) + _zscore_rolling(volume, 60)) / 2
    return _rolling_mean(base, 252)

def dsen_181_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 121 distress score ensemble by measuring deviations from the 5d mean.
    """
    base = (_zscore_rolling(close, 60) + _zscore_rolling(volume, 60)) / 2
    return _zscore_rolling(base, 5)

def dsen_182_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 121 distress score ensemble by measuring deviations from the 21d mean.
    """
    base = (_zscore_rolling(close, 60) + _zscore_rolling(volume, 60)) / 2
    return _zscore_rolling(base, 21)

def dsen_183_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 121 distress score ensemble by measuring deviations from the 63d mean.
    """
    base = (_zscore_rolling(close, 60) + _zscore_rolling(volume, 60)) / 2
    return _zscore_rolling(base, 63)

def dsen_184_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 121 distress score ensemble by measuring deviations from the 126d mean.
    """
    base = (_zscore_rolling(close, 60) + _zscore_rolling(volume, 60)) / 2
    return _zscore_rolling(base, 126)

def dsen_185_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 121 distress score ensemble by measuring deviations from the 252d mean.
    """
    base = (_zscore_rolling(close, 60) + _zscore_rolling(volume, 60)) / 2
    return _zscore_rolling(base, 252)

def dsen_186_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 121 distress score ensemble to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = (_zscore_rolling(close, 60) + _zscore_rolling(volume, 60)) / 2
    return _rank_pct(base, 5)

def dsen_187_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 121 distress score ensemble to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = (_zscore_rolling(close, 60) + _zscore_rolling(volume, 60)) / 2
    return _rank_pct(base, 21)

def dsen_188_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 121 distress score ensemble to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = (_zscore_rolling(close, 60) + _zscore_rolling(volume, 60)) / 2
    return _rank_pct(base, 63)

def dsen_189_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 121 distress score ensemble to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = (_zscore_rolling(close, 60) + _zscore_rolling(volume, 60)) / 2
    return _rank_pct(base, 126)

def dsen_190_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 121 distress score ensemble to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = (_zscore_rolling(close, 60) + _zscore_rolling(volume, 60)) / 2
    return _rank_pct(base, 252)

def dsen_191_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 121 distress score ensemble distribution over 5d to detect tail risk or exhaustion.
    """
    base = (_zscore_rolling(close, 60) + _zscore_rolling(volume, 60)) / 2
    return _rolling_skew(base, 5)

def dsen_192_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 121 distress score ensemble distribution over 21d to detect tail risk or exhaustion.
    """
    base = (_zscore_rolling(close, 60) + _zscore_rolling(volume, 60)) / 2
    return _rolling_skew(base, 21)

def dsen_193_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 121 distress score ensemble distribution over 63d to detect tail risk or exhaustion.
    """
    base = (_zscore_rolling(close, 60) + _zscore_rolling(volume, 60)) / 2
    return _rolling_skew(base, 63)

def dsen_194_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 121 distress score ensemble distribution over 126d to detect tail risk or exhaustion.
    """
    base = (_zscore_rolling(close, 60) + _zscore_rolling(volume, 60)) / 2
    return _rolling_skew(base, 126)

def dsen_195_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 121 distress score ensemble distribution over 252d to detect tail risk or exhaustion.
    """
    base = (_zscore_rolling(close, 60) + _zscore_rolling(volume, 60)) / 2
    return _rolling_skew(base, 252)

def dsen_196_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 121 distress score ensemble over 5d to capture explosive breakdown or reversal points.
    """
    base = (_zscore_rolling(close, 60) + _zscore_rolling(volume, 60)) / 2
    return _rolling_kurt(base, 5)

def dsen_197_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 121 distress score ensemble over 21d to capture explosive breakdown or reversal points.
    """
    base = (_zscore_rolling(close, 60) + _zscore_rolling(volume, 60)) / 2
    return _rolling_kurt(base, 21)

def dsen_198_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 121 distress score ensemble over 63d to capture explosive breakdown or reversal points.
    """
    base = (_zscore_rolling(close, 60) + _zscore_rolling(volume, 60)) / 2
    return _rolling_kurt(base, 63)

def dsen_199_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 121 distress score ensemble over 126d to capture explosive breakdown or reversal points.
    """
    base = (_zscore_rolling(close, 60) + _zscore_rolling(volume, 60)) / 2
    return _rolling_kurt(base, 126)

def dsen_200_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 121 distress score ensemble over 252d to capture explosive breakdown or reversal points.
    """
    base = (_zscore_rolling(close, 60) + _zscore_rolling(volume, 60)) / 2
    return _rolling_kurt(base, 252)

def dsen_201_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 121 distress score ensemble for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = (_zscore_rolling(close, 60) + _zscore_rolling(volume, 60)) / 2
    return _safe_div(base, _rolling_std(base, 5))

def dsen_202_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 121 distress score ensemble for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = (_zscore_rolling(close, 60) + _zscore_rolling(volume, 60)) / 2
    return _safe_div(base, _rolling_std(base, 21))

def dsen_203_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 121 distress score ensemble for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = (_zscore_rolling(close, 60) + _zscore_rolling(volume, 60)) / 2
    return _safe_div(base, _rolling_std(base, 63))

def dsen_204_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 121 distress score ensemble for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = (_zscore_rolling(close, 60) + _zscore_rolling(volume, 60)) / 2
    return _safe_div(base, _rolling_std(base, 126))

def dsen_205_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 121 distress score ensemble for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = (_zscore_rolling(close, 60) + _zscore_rolling(volume, 60)) / 2
    return _safe_div(base, _rolling_std(base, 252))

def dsen_206_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 121 distress score ensemble over 5d to stabilize variance and capture exponential shifts.
    """
    base = (_zscore_rolling(close, 60) + _zscore_rolling(volume, 60)) / 2
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def dsen_207_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 121 distress score ensemble over 21d to stabilize variance and capture exponential shifts.
    """
    base = (_zscore_rolling(close, 60) + _zscore_rolling(volume, 60)) / 2
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def dsen_208_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 121 distress score ensemble over 63d to stabilize variance and capture exponential shifts.
    """
    base = (_zscore_rolling(close, 60) + _zscore_rolling(volume, 60)) / 2
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def dsen_209_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 121 distress score ensemble over 126d to stabilize variance and capture exponential shifts.
    """
    base = (_zscore_rolling(close, 60) + _zscore_rolling(volume, 60)) / 2
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def dsen_210_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 121 distress score ensemble over 252d to stabilize variance and capture exponential shifts.
    """
    base = (_zscore_rolling(close, 60) + _zscore_rolling(volume, 60)) / 2
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def dsen_211_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 121 distress score ensemble over a 5d horizon to identify extreme regimes.
    """
    base = (_zscore_rolling(close, 70) + _zscore_rolling(volume, 70)) / 2
    return _rolling_mean(base, 5)

def dsen_212_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 121 distress score ensemble over a 21d horizon to identify extreme regimes.
    """
    base = (_zscore_rolling(close, 70) + _zscore_rolling(volume, 70)) / 2
    return _rolling_mean(base, 21)

def dsen_213_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 121 distress score ensemble over a 63d horizon to identify extreme regimes.
    """
    base = (_zscore_rolling(close, 70) + _zscore_rolling(volume, 70)) / 2
    return _rolling_mean(base, 63)

def dsen_214_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 121 distress score ensemble over a 126d horizon to identify extreme regimes.
    """
    base = (_zscore_rolling(close, 70) + _zscore_rolling(volume, 70)) / 2
    return _rolling_mean(base, 126)

def dsen_215_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 121 distress score ensemble over a 252d horizon to identify extreme regimes.
    """
    base = (_zscore_rolling(close, 70) + _zscore_rolling(volume, 70)) / 2
    return _rolling_mean(base, 252)

def dsen_216_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 121 distress score ensemble by measuring deviations from the 5d mean.
    """
    base = (_zscore_rolling(close, 70) + _zscore_rolling(volume, 70)) / 2
    return _zscore_rolling(base, 5)

def dsen_217_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 121 distress score ensemble by measuring deviations from the 21d mean.
    """
    base = (_zscore_rolling(close, 70) + _zscore_rolling(volume, 70)) / 2
    return _zscore_rolling(base, 21)

def dsen_218_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 121 distress score ensemble by measuring deviations from the 63d mean.
    """
    base = (_zscore_rolling(close, 70) + _zscore_rolling(volume, 70)) / 2
    return _zscore_rolling(base, 63)

def dsen_219_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 121 distress score ensemble by measuring deviations from the 126d mean.
    """
    base = (_zscore_rolling(close, 70) + _zscore_rolling(volume, 70)) / 2
    return _zscore_rolling(base, 126)

def dsen_220_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 121 distress score ensemble by measuring deviations from the 252d mean.
    """
    base = (_zscore_rolling(close, 70) + _zscore_rolling(volume, 70)) / 2
    return _zscore_rolling(base, 252)

def dsen_221_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 121 distress score ensemble to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = (_zscore_rolling(close, 70) + _zscore_rolling(volume, 70)) / 2
    return _rank_pct(base, 5)

def dsen_222_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 121 distress score ensemble to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = (_zscore_rolling(close, 70) + _zscore_rolling(volume, 70)) / 2
    return _rank_pct(base, 21)

def dsen_223_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 121 distress score ensemble to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = (_zscore_rolling(close, 70) + _zscore_rolling(volume, 70)) / 2
    return _rank_pct(base, 63)

def dsen_224_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 121 distress score ensemble to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = (_zscore_rolling(close, 70) + _zscore_rolling(volume, 70)) / 2
    return _rank_pct(base, 126)

def dsen_225_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 121 distress score ensemble to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = (_zscore_rolling(close, 70) + _zscore_rolling(volume, 70)) / 2
    return _rank_pct(base, 252)
