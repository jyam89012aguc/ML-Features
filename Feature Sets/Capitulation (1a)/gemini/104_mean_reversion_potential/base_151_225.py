"""
104_104_mean_reversion_potential — Base Features 151-225
Domain: 104_mean_reversion_potential
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

def mrpt_151_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 104 mean reversion potential to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = close / _rolling_mean(close, 85) - 1
    return _rank_pct(base, 5)

def mrpt_152_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 104 mean reversion potential to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = close / _rolling_mean(close, 85) - 1
    return _rank_pct(base, 21)

def mrpt_153_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 104 mean reversion potential to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = close / _rolling_mean(close, 85) - 1
    return _rank_pct(base, 63)

def mrpt_154_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 104 mean reversion potential to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = close / _rolling_mean(close, 85) - 1
    return _rank_pct(base, 126)

def mrpt_155_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 104 mean reversion potential to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = close / _rolling_mean(close, 85) - 1
    return _rank_pct(base, 252)

def mrpt_156_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 104 mean reversion potential distribution over 5d to detect tail risk or exhaustion.
    """
    base = close / _rolling_mean(close, 85) - 1
    return _rolling_skew(base, 5)

def mrpt_157_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 104 mean reversion potential distribution over 21d to detect tail risk or exhaustion.
    """
    base = close / _rolling_mean(close, 85) - 1
    return _rolling_skew(base, 21)

def mrpt_158_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 104 mean reversion potential distribution over 63d to detect tail risk or exhaustion.
    """
    base = close / _rolling_mean(close, 85) - 1
    return _rolling_skew(base, 63)

def mrpt_159_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 104 mean reversion potential distribution over 126d to detect tail risk or exhaustion.
    """
    base = close / _rolling_mean(close, 85) - 1
    return _rolling_skew(base, 126)

def mrpt_160_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 104 mean reversion potential distribution over 252d to detect tail risk or exhaustion.
    """
    base = close / _rolling_mean(close, 85) - 1
    return _rolling_skew(base, 252)

def mrpt_161_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 104 mean reversion potential over 5d to capture explosive breakdown or reversal points.
    """
    base = close / _rolling_mean(close, 85) - 1
    return _rolling_kurt(base, 5)

def mrpt_162_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 104 mean reversion potential over 21d to capture explosive breakdown or reversal points.
    """
    base = close / _rolling_mean(close, 85) - 1
    return _rolling_kurt(base, 21)

def mrpt_163_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 104 mean reversion potential over 63d to capture explosive breakdown or reversal points.
    """
    base = close / _rolling_mean(close, 85) - 1
    return _rolling_kurt(base, 63)

def mrpt_164_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 104 mean reversion potential over 126d to capture explosive breakdown or reversal points.
    """
    base = close / _rolling_mean(close, 85) - 1
    return _rolling_kurt(base, 126)

def mrpt_165_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 104 mean reversion potential over 252d to capture explosive breakdown or reversal points.
    """
    base = close / _rolling_mean(close, 85) - 1
    return _rolling_kurt(base, 252)

def mrpt_166_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 104 mean reversion potential for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = close / _rolling_mean(close, 85) - 1
    return _safe_div(base, _rolling_std(base, 5))

def mrpt_167_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 104 mean reversion potential for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = close / _rolling_mean(close, 85) - 1
    return _safe_div(base, _rolling_std(base, 21))

def mrpt_168_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 104 mean reversion potential for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = close / _rolling_mean(close, 85) - 1
    return _safe_div(base, _rolling_std(base, 63))

def mrpt_169_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 104 mean reversion potential for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = close / _rolling_mean(close, 85) - 1
    return _safe_div(base, _rolling_std(base, 126))

def mrpt_170_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 104 mean reversion potential for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = close / _rolling_mean(close, 85) - 1
    return _safe_div(base, _rolling_std(base, 252))

def mrpt_171_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 104 mean reversion potential over 5d to stabilize variance and capture exponential shifts.
    """
    base = close / _rolling_mean(close, 85) - 1
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def mrpt_172_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 104 mean reversion potential over 21d to stabilize variance and capture exponential shifts.
    """
    base = close / _rolling_mean(close, 85) - 1
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def mrpt_173_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 104 mean reversion potential over 63d to stabilize variance and capture exponential shifts.
    """
    base = close / _rolling_mean(close, 85) - 1
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def mrpt_174_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 104 mean reversion potential over 126d to stabilize variance and capture exponential shifts.
    """
    base = close / _rolling_mean(close, 85) - 1
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def mrpt_175_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 104 mean reversion potential over 252d to stabilize variance and capture exponential shifts.
    """
    base = close / _rolling_mean(close, 85) - 1
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def mrpt_176_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 104 mean reversion potential over a 5d horizon to identify extreme regimes.
    """
    base = close / _rolling_mean(close, 105) - 1
    return _rolling_mean(base, 5)

def mrpt_177_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 104 mean reversion potential over a 21d horizon to identify extreme regimes.
    """
    base = close / _rolling_mean(close, 105) - 1
    return _rolling_mean(base, 21)

def mrpt_178_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 104 mean reversion potential over a 63d horizon to identify extreme regimes.
    """
    base = close / _rolling_mean(close, 105) - 1
    return _rolling_mean(base, 63)

def mrpt_179_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 104 mean reversion potential over a 126d horizon to identify extreme regimes.
    """
    base = close / _rolling_mean(close, 105) - 1
    return _rolling_mean(base, 126)

def mrpt_180_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 104 mean reversion potential over a 252d horizon to identify extreme regimes.
    """
    base = close / _rolling_mean(close, 105) - 1
    return _rolling_mean(base, 252)

def mrpt_181_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 104 mean reversion potential by measuring deviations from the 5d mean.
    """
    base = close / _rolling_mean(close, 105) - 1
    return _zscore_rolling(base, 5)

def mrpt_182_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 104 mean reversion potential by measuring deviations from the 21d mean.
    """
    base = close / _rolling_mean(close, 105) - 1
    return _zscore_rolling(base, 21)

def mrpt_183_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 104 mean reversion potential by measuring deviations from the 63d mean.
    """
    base = close / _rolling_mean(close, 105) - 1
    return _zscore_rolling(base, 63)

def mrpt_184_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 104 mean reversion potential by measuring deviations from the 126d mean.
    """
    base = close / _rolling_mean(close, 105) - 1
    return _zscore_rolling(base, 126)

def mrpt_185_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 104 mean reversion potential by measuring deviations from the 252d mean.
    """
    base = close / _rolling_mean(close, 105) - 1
    return _zscore_rolling(base, 252)

def mrpt_186_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 104 mean reversion potential to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = close / _rolling_mean(close, 105) - 1
    return _rank_pct(base, 5)

def mrpt_187_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 104 mean reversion potential to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = close / _rolling_mean(close, 105) - 1
    return _rank_pct(base, 21)

def mrpt_188_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 104 mean reversion potential to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = close / _rolling_mean(close, 105) - 1
    return _rank_pct(base, 63)

def mrpt_189_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 104 mean reversion potential to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = close / _rolling_mean(close, 105) - 1
    return _rank_pct(base, 126)

def mrpt_190_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 104 mean reversion potential to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = close / _rolling_mean(close, 105) - 1
    return _rank_pct(base, 252)

def mrpt_191_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 104 mean reversion potential distribution over 5d to detect tail risk or exhaustion.
    """
    base = close / _rolling_mean(close, 105) - 1
    return _rolling_skew(base, 5)

def mrpt_192_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 104 mean reversion potential distribution over 21d to detect tail risk or exhaustion.
    """
    base = close / _rolling_mean(close, 105) - 1
    return _rolling_skew(base, 21)

def mrpt_193_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 104 mean reversion potential distribution over 63d to detect tail risk or exhaustion.
    """
    base = close / _rolling_mean(close, 105) - 1
    return _rolling_skew(base, 63)

def mrpt_194_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 104 mean reversion potential distribution over 126d to detect tail risk or exhaustion.
    """
    base = close / _rolling_mean(close, 105) - 1
    return _rolling_skew(base, 126)

def mrpt_195_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 104 mean reversion potential distribution over 252d to detect tail risk or exhaustion.
    """
    base = close / _rolling_mean(close, 105) - 1
    return _rolling_skew(base, 252)

def mrpt_196_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 104 mean reversion potential over 5d to capture explosive breakdown or reversal points.
    """
    base = close / _rolling_mean(close, 105) - 1
    return _rolling_kurt(base, 5)

def mrpt_197_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 104 mean reversion potential over 21d to capture explosive breakdown or reversal points.
    """
    base = close / _rolling_mean(close, 105) - 1
    return _rolling_kurt(base, 21)

def mrpt_198_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 104 mean reversion potential over 63d to capture explosive breakdown or reversal points.
    """
    base = close / _rolling_mean(close, 105) - 1
    return _rolling_kurt(base, 63)

def mrpt_199_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 104 mean reversion potential over 126d to capture explosive breakdown or reversal points.
    """
    base = close / _rolling_mean(close, 105) - 1
    return _rolling_kurt(base, 126)

def mrpt_200_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 104 mean reversion potential over 252d to capture explosive breakdown or reversal points.
    """
    base = close / _rolling_mean(close, 105) - 1
    return _rolling_kurt(base, 252)

def mrpt_201_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 104 mean reversion potential for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = close / _rolling_mean(close, 105) - 1
    return _safe_div(base, _rolling_std(base, 5))

def mrpt_202_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 104 mean reversion potential for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = close / _rolling_mean(close, 105) - 1
    return _safe_div(base, _rolling_std(base, 21))

def mrpt_203_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 104 mean reversion potential for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = close / _rolling_mean(close, 105) - 1
    return _safe_div(base, _rolling_std(base, 63))

def mrpt_204_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 104 mean reversion potential for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = close / _rolling_mean(close, 105) - 1
    return _safe_div(base, _rolling_std(base, 126))

def mrpt_205_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 104 mean reversion potential for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = close / _rolling_mean(close, 105) - 1
    return _safe_div(base, _rolling_std(base, 252))

def mrpt_206_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 104 mean reversion potential over 5d to stabilize variance and capture exponential shifts.
    """
    base = close / _rolling_mean(close, 105) - 1
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def mrpt_207_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 104 mean reversion potential over 21d to stabilize variance and capture exponential shifts.
    """
    base = close / _rolling_mean(close, 105) - 1
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def mrpt_208_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 104 mean reversion potential over 63d to stabilize variance and capture exponential shifts.
    """
    base = close / _rolling_mean(close, 105) - 1
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def mrpt_209_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 104 mean reversion potential over 126d to stabilize variance and capture exponential shifts.
    """
    base = close / _rolling_mean(close, 105) - 1
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def mrpt_210_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 104 mean reversion potential over 252d to stabilize variance and capture exponential shifts.
    """
    base = close / _rolling_mean(close, 105) - 1
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def mrpt_211_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 104 mean reversion potential over a 5d horizon to identify extreme regimes.
    """
    base = close / _rolling_mean(close, 125) - 1
    return _rolling_mean(base, 5)

def mrpt_212_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 104 mean reversion potential over a 21d horizon to identify extreme regimes.
    """
    base = close / _rolling_mean(close, 125) - 1
    return _rolling_mean(base, 21)

def mrpt_213_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 104 mean reversion potential over a 63d horizon to identify extreme regimes.
    """
    base = close / _rolling_mean(close, 125) - 1
    return _rolling_mean(base, 63)

def mrpt_214_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 104 mean reversion potential over a 126d horizon to identify extreme regimes.
    """
    base = close / _rolling_mean(close, 125) - 1
    return _rolling_mean(base, 126)

def mrpt_215_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 104 mean reversion potential over a 252d horizon to identify extreme regimes.
    """
    base = close / _rolling_mean(close, 125) - 1
    return _rolling_mean(base, 252)

def mrpt_216_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 104 mean reversion potential by measuring deviations from the 5d mean.
    """
    base = close / _rolling_mean(close, 125) - 1
    return _zscore_rolling(base, 5)

def mrpt_217_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 104 mean reversion potential by measuring deviations from the 21d mean.
    """
    base = close / _rolling_mean(close, 125) - 1
    return _zscore_rolling(base, 21)

def mrpt_218_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 104 mean reversion potential by measuring deviations from the 63d mean.
    """
    base = close / _rolling_mean(close, 125) - 1
    return _zscore_rolling(base, 63)

def mrpt_219_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 104 mean reversion potential by measuring deviations from the 126d mean.
    """
    base = close / _rolling_mean(close, 125) - 1
    return _zscore_rolling(base, 126)

def mrpt_220_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 104 mean reversion potential by measuring deviations from the 252d mean.
    """
    base = close / _rolling_mean(close, 125) - 1
    return _zscore_rolling(base, 252)

def mrpt_221_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 104 mean reversion potential to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = close / _rolling_mean(close, 125) - 1
    return _rank_pct(base, 5)

def mrpt_222_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 104 mean reversion potential to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = close / _rolling_mean(close, 125) - 1
    return _rank_pct(base, 21)

def mrpt_223_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 104 mean reversion potential to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = close / _rolling_mean(close, 125) - 1
    return _rank_pct(base, 63)

def mrpt_224_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 104 mean reversion potential to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = close / _rolling_mean(close, 125) - 1
    return _rank_pct(base, 126)

def mrpt_225_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 104 mean reversion potential to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = close / _rolling_mean(close, 125) - 1
    return _rank_pct(base, 252)
