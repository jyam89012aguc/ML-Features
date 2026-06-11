"""
107_107_change_point_detection — Base Features 151-225
Domain: 107_change_point_detection
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

def cpdt_151_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 107 change point detection to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(25).std().diff()
    return _rank_pct(base, 5)

def cpdt_152_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 107 change point detection to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(25).std().diff()
    return _rank_pct(base, 21)

def cpdt_153_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 107 change point detection to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(25).std().diff()
    return _rank_pct(base, 63)

def cpdt_154_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 107 change point detection to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(25).std().diff()
    return _rank_pct(base, 126)

def cpdt_155_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 107 change point detection to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(25).std().diff()
    return _rank_pct(base, 252)

def cpdt_156_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 107 change point detection distribution over 5d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(25).std().diff()
    return _rolling_skew(base, 5)

def cpdt_157_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 107 change point detection distribution over 21d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(25).std().diff()
    return _rolling_skew(base, 21)

def cpdt_158_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 107 change point detection distribution over 63d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(25).std().diff()
    return _rolling_skew(base, 63)

def cpdt_159_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 107 change point detection distribution over 126d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(25).std().diff()
    return _rolling_skew(base, 126)

def cpdt_160_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 107 change point detection distribution over 252d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(25).std().diff()
    return _rolling_skew(base, 252)

def cpdt_161_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 107 change point detection over 5d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(25).std().diff()
    return _rolling_kurt(base, 5)

def cpdt_162_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 107 change point detection over 21d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(25).std().diff()
    return _rolling_kurt(base, 21)

def cpdt_163_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 107 change point detection over 63d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(25).std().diff()
    return _rolling_kurt(base, 63)

def cpdt_164_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 107 change point detection over 126d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(25).std().diff()
    return _rolling_kurt(base, 126)

def cpdt_165_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 107 change point detection over 252d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(25).std().diff()
    return _rolling_kurt(base, 252)

def cpdt_166_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 107 change point detection for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(25).std().diff()
    return _safe_div(base, _rolling_std(base, 5))

def cpdt_167_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 107 change point detection for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(25).std().diff()
    return _safe_div(base, _rolling_std(base, 21))

def cpdt_168_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 107 change point detection for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(25).std().diff()
    return _safe_div(base, _rolling_std(base, 63))

def cpdt_169_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 107 change point detection for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(25).std().diff()
    return _safe_div(base, _rolling_std(base, 126))

def cpdt_170_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 107 change point detection for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(25).std().diff()
    return _safe_div(base, _rolling_std(base, 252))

def cpdt_171_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 107 change point detection over 5d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(25).std().diff()
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def cpdt_172_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 107 change point detection over 21d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(25).std().diff()
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def cpdt_173_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 107 change point detection over 63d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(25).std().diff()
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def cpdt_174_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 107 change point detection over 126d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(25).std().diff()
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def cpdt_175_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 107 change point detection over 252d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(25).std().diff()
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def cpdt_176_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 107 change point detection over a 5d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(30).std().diff()
    return _rolling_mean(base, 5)

def cpdt_177_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 107 change point detection over a 21d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(30).std().diff()
    return _rolling_mean(base, 21)

def cpdt_178_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 107 change point detection over a 63d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(30).std().diff()
    return _rolling_mean(base, 63)

def cpdt_179_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 107 change point detection over a 126d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(30).std().diff()
    return _rolling_mean(base, 126)

def cpdt_180_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 107 change point detection over a 252d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(30).std().diff()
    return _rolling_mean(base, 252)

def cpdt_181_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 107 change point detection by measuring deviations from the 5d mean.
    """
    base = close.pct_change().rolling(30).std().diff()
    return _zscore_rolling(base, 5)

def cpdt_182_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 107 change point detection by measuring deviations from the 21d mean.
    """
    base = close.pct_change().rolling(30).std().diff()
    return _zscore_rolling(base, 21)

def cpdt_183_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 107 change point detection by measuring deviations from the 63d mean.
    """
    base = close.pct_change().rolling(30).std().diff()
    return _zscore_rolling(base, 63)

def cpdt_184_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 107 change point detection by measuring deviations from the 126d mean.
    """
    base = close.pct_change().rolling(30).std().diff()
    return _zscore_rolling(base, 126)

def cpdt_185_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 107 change point detection by measuring deviations from the 252d mean.
    """
    base = close.pct_change().rolling(30).std().diff()
    return _zscore_rolling(base, 252)

def cpdt_186_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 107 change point detection to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(30).std().diff()
    return _rank_pct(base, 5)

def cpdt_187_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 107 change point detection to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(30).std().diff()
    return _rank_pct(base, 21)

def cpdt_188_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 107 change point detection to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(30).std().diff()
    return _rank_pct(base, 63)

def cpdt_189_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 107 change point detection to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(30).std().diff()
    return _rank_pct(base, 126)

def cpdt_190_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 107 change point detection to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(30).std().diff()
    return _rank_pct(base, 252)

def cpdt_191_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 107 change point detection distribution over 5d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(30).std().diff()
    return _rolling_skew(base, 5)

def cpdt_192_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 107 change point detection distribution over 21d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(30).std().diff()
    return _rolling_skew(base, 21)

def cpdt_193_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 107 change point detection distribution over 63d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(30).std().diff()
    return _rolling_skew(base, 63)

def cpdt_194_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 107 change point detection distribution over 126d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(30).std().diff()
    return _rolling_skew(base, 126)

def cpdt_195_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 107 change point detection distribution over 252d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(30).std().diff()
    return _rolling_skew(base, 252)

def cpdt_196_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 107 change point detection over 5d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(30).std().diff()
    return _rolling_kurt(base, 5)

def cpdt_197_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 107 change point detection over 21d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(30).std().diff()
    return _rolling_kurt(base, 21)

def cpdt_198_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 107 change point detection over 63d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(30).std().diff()
    return _rolling_kurt(base, 63)

def cpdt_199_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 107 change point detection over 126d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(30).std().diff()
    return _rolling_kurt(base, 126)

def cpdt_200_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 107 change point detection over 252d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(30).std().diff()
    return _rolling_kurt(base, 252)

def cpdt_201_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 107 change point detection for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(30).std().diff()
    return _safe_div(base, _rolling_std(base, 5))

def cpdt_202_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 107 change point detection for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(30).std().diff()
    return _safe_div(base, _rolling_std(base, 21))

def cpdt_203_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 107 change point detection for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(30).std().diff()
    return _safe_div(base, _rolling_std(base, 63))

def cpdt_204_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 107 change point detection for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(30).std().diff()
    return _safe_div(base, _rolling_std(base, 126))

def cpdt_205_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 107 change point detection for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(30).std().diff()
    return _safe_div(base, _rolling_std(base, 252))

def cpdt_206_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 107 change point detection over 5d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(30).std().diff()
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def cpdt_207_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 107 change point detection over 21d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(30).std().diff()
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def cpdt_208_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 107 change point detection over 63d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(30).std().diff()
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def cpdt_209_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 107 change point detection over 126d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(30).std().diff()
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def cpdt_210_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 107 change point detection over 252d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(30).std().diff()
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def cpdt_211_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 107 change point detection over a 5d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(35).std().diff()
    return _rolling_mean(base, 5)

def cpdt_212_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 107 change point detection over a 21d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(35).std().diff()
    return _rolling_mean(base, 21)

def cpdt_213_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 107 change point detection over a 63d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(35).std().diff()
    return _rolling_mean(base, 63)

def cpdt_214_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 107 change point detection over a 126d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(35).std().diff()
    return _rolling_mean(base, 126)

def cpdt_215_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 107 change point detection over a 252d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(35).std().diff()
    return _rolling_mean(base, 252)

def cpdt_216_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 107 change point detection by measuring deviations from the 5d mean.
    """
    base = close.pct_change().rolling(35).std().diff()
    return _zscore_rolling(base, 5)

def cpdt_217_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 107 change point detection by measuring deviations from the 21d mean.
    """
    base = close.pct_change().rolling(35).std().diff()
    return _zscore_rolling(base, 21)

def cpdt_218_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 107 change point detection by measuring deviations from the 63d mean.
    """
    base = close.pct_change().rolling(35).std().diff()
    return _zscore_rolling(base, 63)

def cpdt_219_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 107 change point detection by measuring deviations from the 126d mean.
    """
    base = close.pct_change().rolling(35).std().diff()
    return _zscore_rolling(base, 126)

def cpdt_220_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 107 change point detection by measuring deviations from the 252d mean.
    """
    base = close.pct_change().rolling(35).std().diff()
    return _zscore_rolling(base, 252)

def cpdt_221_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 107 change point detection to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(35).std().diff()
    return _rank_pct(base, 5)

def cpdt_222_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 107 change point detection to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(35).std().diff()
    return _rank_pct(base, 21)

def cpdt_223_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 107 change point detection to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(35).std().diff()
    return _rank_pct(base, 63)

def cpdt_224_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 107 change point detection to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(35).std().diff()
    return _rank_pct(base, 126)

def cpdt_225_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 107 change point detection to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(35).std().diff()
    return _rank_pct(base, 252)
