"""
122_122_capital_access_stress — Base Features 151-225
Domain: 122_capital_access_stress
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

def cast_151_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 122 capital access stress to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(25).std()
    return _rank_pct(base, 5)

def cast_152_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 122 capital access stress to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(25).std()
    return _rank_pct(base, 21)

def cast_153_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 122 capital access stress to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(25).std()
    return _rank_pct(base, 63)

def cast_154_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 122 capital access stress to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(25).std()
    return _rank_pct(base, 126)

def cast_155_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 122 capital access stress to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(25).std()
    return _rank_pct(base, 252)

def cast_156_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 122 capital access stress distribution over 5d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(25).std()
    return _rolling_skew(base, 5)

def cast_157_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 122 capital access stress distribution over 21d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(25).std()
    return _rolling_skew(base, 21)

def cast_158_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 122 capital access stress distribution over 63d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(25).std()
    return _rolling_skew(base, 63)

def cast_159_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 122 capital access stress distribution over 126d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(25).std()
    return _rolling_skew(base, 126)

def cast_160_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 122 capital access stress distribution over 252d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(25).std()
    return _rolling_skew(base, 252)

def cast_161_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 122 capital access stress over 5d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(25).std()
    return _rolling_kurt(base, 5)

def cast_162_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 122 capital access stress over 21d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(25).std()
    return _rolling_kurt(base, 21)

def cast_163_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 122 capital access stress over 63d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(25).std()
    return _rolling_kurt(base, 63)

def cast_164_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 122 capital access stress over 126d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(25).std()
    return _rolling_kurt(base, 126)

def cast_165_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 122 capital access stress over 252d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(25).std()
    return _rolling_kurt(base, 252)

def cast_166_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 122 capital access stress for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(25).std()
    return _safe_div(base, _rolling_std(base, 5))

def cast_167_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 122 capital access stress for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(25).std()
    return _safe_div(base, _rolling_std(base, 21))

def cast_168_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 122 capital access stress for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(25).std()
    return _safe_div(base, _rolling_std(base, 63))

def cast_169_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 122 capital access stress for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(25).std()
    return _safe_div(base, _rolling_std(base, 126))

def cast_170_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 122 capital access stress for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(25).std()
    return _safe_div(base, _rolling_std(base, 252))

def cast_171_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 122 capital access stress over 5d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(25).std()
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def cast_172_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 122 capital access stress over 21d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(25).std()
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def cast_173_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 122 capital access stress over 63d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(25).std()
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def cast_174_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 122 capital access stress over 126d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(25).std()
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def cast_175_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 122 capital access stress over 252d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(25).std()
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def cast_176_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 122 capital access stress over a 5d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(30).std()
    return _rolling_mean(base, 5)

def cast_177_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 122 capital access stress over a 21d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(30).std()
    return _rolling_mean(base, 21)

def cast_178_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 122 capital access stress over a 63d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(30).std()
    return _rolling_mean(base, 63)

def cast_179_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 122 capital access stress over a 126d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(30).std()
    return _rolling_mean(base, 126)

def cast_180_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 122 capital access stress over a 252d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(30).std()
    return _rolling_mean(base, 252)

def cast_181_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 122 capital access stress by measuring deviations from the 5d mean.
    """
    base = close.pct_change().rolling(30).std()
    return _zscore_rolling(base, 5)

def cast_182_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 122 capital access stress by measuring deviations from the 21d mean.
    """
    base = close.pct_change().rolling(30).std()
    return _zscore_rolling(base, 21)

def cast_183_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 122 capital access stress by measuring deviations from the 63d mean.
    """
    base = close.pct_change().rolling(30).std()
    return _zscore_rolling(base, 63)

def cast_184_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 122 capital access stress by measuring deviations from the 126d mean.
    """
    base = close.pct_change().rolling(30).std()
    return _zscore_rolling(base, 126)

def cast_185_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 122 capital access stress by measuring deviations from the 252d mean.
    """
    base = close.pct_change().rolling(30).std()
    return _zscore_rolling(base, 252)

def cast_186_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 122 capital access stress to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(30).std()
    return _rank_pct(base, 5)

def cast_187_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 122 capital access stress to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(30).std()
    return _rank_pct(base, 21)

def cast_188_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 122 capital access stress to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(30).std()
    return _rank_pct(base, 63)

def cast_189_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 122 capital access stress to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(30).std()
    return _rank_pct(base, 126)

def cast_190_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 122 capital access stress to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(30).std()
    return _rank_pct(base, 252)

def cast_191_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 122 capital access stress distribution over 5d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(30).std()
    return _rolling_skew(base, 5)

def cast_192_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 122 capital access stress distribution over 21d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(30).std()
    return _rolling_skew(base, 21)

def cast_193_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 122 capital access stress distribution over 63d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(30).std()
    return _rolling_skew(base, 63)

def cast_194_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 122 capital access stress distribution over 126d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(30).std()
    return _rolling_skew(base, 126)

def cast_195_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 122 capital access stress distribution over 252d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(30).std()
    return _rolling_skew(base, 252)

def cast_196_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 122 capital access stress over 5d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(30).std()
    return _rolling_kurt(base, 5)

def cast_197_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 122 capital access stress over 21d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(30).std()
    return _rolling_kurt(base, 21)

def cast_198_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 122 capital access stress over 63d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(30).std()
    return _rolling_kurt(base, 63)

def cast_199_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 122 capital access stress over 126d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(30).std()
    return _rolling_kurt(base, 126)

def cast_200_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 122 capital access stress over 252d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(30).std()
    return _rolling_kurt(base, 252)

def cast_201_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 122 capital access stress for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(30).std()
    return _safe_div(base, _rolling_std(base, 5))

def cast_202_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 122 capital access stress for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(30).std()
    return _safe_div(base, _rolling_std(base, 21))

def cast_203_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 122 capital access stress for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(30).std()
    return _safe_div(base, _rolling_std(base, 63))

def cast_204_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 122 capital access stress for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(30).std()
    return _safe_div(base, _rolling_std(base, 126))

def cast_205_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 122 capital access stress for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(30).std()
    return _safe_div(base, _rolling_std(base, 252))

def cast_206_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 122 capital access stress over 5d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(30).std()
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def cast_207_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 122 capital access stress over 21d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(30).std()
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def cast_208_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 122 capital access stress over 63d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(30).std()
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def cast_209_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 122 capital access stress over 126d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(30).std()
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def cast_210_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 122 capital access stress over 252d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(30).std()
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def cast_211_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 122 capital access stress over a 5d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(35).std()
    return _rolling_mean(base, 5)

def cast_212_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 122 capital access stress over a 21d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(35).std()
    return _rolling_mean(base, 21)

def cast_213_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 122 capital access stress over a 63d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(35).std()
    return _rolling_mean(base, 63)

def cast_214_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 122 capital access stress over a 126d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(35).std()
    return _rolling_mean(base, 126)

def cast_215_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 122 capital access stress over a 252d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(35).std()
    return _rolling_mean(base, 252)

def cast_216_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 122 capital access stress by measuring deviations from the 5d mean.
    """
    base = close.pct_change().rolling(35).std()
    return _zscore_rolling(base, 5)

def cast_217_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 122 capital access stress by measuring deviations from the 21d mean.
    """
    base = close.pct_change().rolling(35).std()
    return _zscore_rolling(base, 21)

def cast_218_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 122 capital access stress by measuring deviations from the 63d mean.
    """
    base = close.pct_change().rolling(35).std()
    return _zscore_rolling(base, 63)

def cast_219_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 122 capital access stress by measuring deviations from the 126d mean.
    """
    base = close.pct_change().rolling(35).std()
    return _zscore_rolling(base, 126)

def cast_220_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 122 capital access stress by measuring deviations from the 252d mean.
    """
    base = close.pct_change().rolling(35).std()
    return _zscore_rolling(base, 252)

def cast_221_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 122 capital access stress to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(35).std()
    return _rank_pct(base, 5)

def cast_222_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 122 capital access stress to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(35).std()
    return _rank_pct(base, 21)

def cast_223_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 122 capital access stress to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(35).std()
    return _rank_pct(base, 63)

def cast_224_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 122 capital access stress to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(35).std()
    return _rank_pct(base, 126)

def cast_225_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 122 capital access stress to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(35).std()
    return _rank_pct(base, 252)
