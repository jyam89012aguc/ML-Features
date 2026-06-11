"""
106_106_support_violation — Base Features 151-225
Domain: 106_support_violation
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

def supv_151_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 106 support violation to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = close / low.rolling(50).min() - 1
    return _rank_pct(base, 5)

def supv_152_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 106 support violation to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = close / low.rolling(50).min() - 1
    return _rank_pct(base, 21)

def supv_153_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 106 support violation to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = close / low.rolling(50).min() - 1
    return _rank_pct(base, 63)

def supv_154_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 106 support violation to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = close / low.rolling(50).min() - 1
    return _rank_pct(base, 126)

def supv_155_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 106 support violation to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = close / low.rolling(50).min() - 1
    return _rank_pct(base, 252)

def supv_156_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 106 support violation distribution over 5d to detect tail risk or exhaustion.
    """
    base = close / low.rolling(50).min() - 1
    return _rolling_skew(base, 5)

def supv_157_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 106 support violation distribution over 21d to detect tail risk or exhaustion.
    """
    base = close / low.rolling(50).min() - 1
    return _rolling_skew(base, 21)

def supv_158_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 106 support violation distribution over 63d to detect tail risk or exhaustion.
    """
    base = close / low.rolling(50).min() - 1
    return _rolling_skew(base, 63)

def supv_159_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 106 support violation distribution over 126d to detect tail risk or exhaustion.
    """
    base = close / low.rolling(50).min() - 1
    return _rolling_skew(base, 126)

def supv_160_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 106 support violation distribution over 252d to detect tail risk or exhaustion.
    """
    base = close / low.rolling(50).min() - 1
    return _rolling_skew(base, 252)

def supv_161_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 106 support violation over 5d to capture explosive breakdown or reversal points.
    """
    base = close / low.rolling(50).min() - 1
    return _rolling_kurt(base, 5)

def supv_162_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 106 support violation over 21d to capture explosive breakdown or reversal points.
    """
    base = close / low.rolling(50).min() - 1
    return _rolling_kurt(base, 21)

def supv_163_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 106 support violation over 63d to capture explosive breakdown or reversal points.
    """
    base = close / low.rolling(50).min() - 1
    return _rolling_kurt(base, 63)

def supv_164_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 106 support violation over 126d to capture explosive breakdown or reversal points.
    """
    base = close / low.rolling(50).min() - 1
    return _rolling_kurt(base, 126)

def supv_165_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 106 support violation over 252d to capture explosive breakdown or reversal points.
    """
    base = close / low.rolling(50).min() - 1
    return _rolling_kurt(base, 252)

def supv_166_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 106 support violation for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = close / low.rolling(50).min() - 1
    return _safe_div(base, _rolling_std(base, 5))

def supv_167_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 106 support violation for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = close / low.rolling(50).min() - 1
    return _safe_div(base, _rolling_std(base, 21))

def supv_168_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 106 support violation for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = close / low.rolling(50).min() - 1
    return _safe_div(base, _rolling_std(base, 63))

def supv_169_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 106 support violation for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = close / low.rolling(50).min() - 1
    return _safe_div(base, _rolling_std(base, 126))

def supv_170_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 106 support violation for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = close / low.rolling(50).min() - 1
    return _safe_div(base, _rolling_std(base, 252))

def supv_171_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 106 support violation over 5d to stabilize variance and capture exponential shifts.
    """
    base = close / low.rolling(50).min() - 1
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def supv_172_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 106 support violation over 21d to stabilize variance and capture exponential shifts.
    """
    base = close / low.rolling(50).min() - 1
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def supv_173_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 106 support violation over 63d to stabilize variance and capture exponential shifts.
    """
    base = close / low.rolling(50).min() - 1
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def supv_174_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 106 support violation over 126d to stabilize variance and capture exponential shifts.
    """
    base = close / low.rolling(50).min() - 1
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def supv_175_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 106 support violation over 252d to stabilize variance and capture exponential shifts.
    """
    base = close / low.rolling(50).min() - 1
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def supv_176_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 106 support violation over a 5d horizon to identify extreme regimes.
    """
    base = close / low.rolling(60).min() - 1
    return _rolling_mean(base, 5)

def supv_177_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 106 support violation over a 21d horizon to identify extreme regimes.
    """
    base = close / low.rolling(60).min() - 1
    return _rolling_mean(base, 21)

def supv_178_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 106 support violation over a 63d horizon to identify extreme regimes.
    """
    base = close / low.rolling(60).min() - 1
    return _rolling_mean(base, 63)

def supv_179_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 106 support violation over a 126d horizon to identify extreme regimes.
    """
    base = close / low.rolling(60).min() - 1
    return _rolling_mean(base, 126)

def supv_180_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 106 support violation over a 252d horizon to identify extreme regimes.
    """
    base = close / low.rolling(60).min() - 1
    return _rolling_mean(base, 252)

def supv_181_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 106 support violation by measuring deviations from the 5d mean.
    """
    base = close / low.rolling(60).min() - 1
    return _zscore_rolling(base, 5)

def supv_182_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 106 support violation by measuring deviations from the 21d mean.
    """
    base = close / low.rolling(60).min() - 1
    return _zscore_rolling(base, 21)

def supv_183_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 106 support violation by measuring deviations from the 63d mean.
    """
    base = close / low.rolling(60).min() - 1
    return _zscore_rolling(base, 63)

def supv_184_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 106 support violation by measuring deviations from the 126d mean.
    """
    base = close / low.rolling(60).min() - 1
    return _zscore_rolling(base, 126)

def supv_185_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 106 support violation by measuring deviations from the 252d mean.
    """
    base = close / low.rolling(60).min() - 1
    return _zscore_rolling(base, 252)

def supv_186_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 106 support violation to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = close / low.rolling(60).min() - 1
    return _rank_pct(base, 5)

def supv_187_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 106 support violation to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = close / low.rolling(60).min() - 1
    return _rank_pct(base, 21)

def supv_188_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 106 support violation to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = close / low.rolling(60).min() - 1
    return _rank_pct(base, 63)

def supv_189_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 106 support violation to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = close / low.rolling(60).min() - 1
    return _rank_pct(base, 126)

def supv_190_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 106 support violation to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = close / low.rolling(60).min() - 1
    return _rank_pct(base, 252)

def supv_191_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 106 support violation distribution over 5d to detect tail risk or exhaustion.
    """
    base = close / low.rolling(60).min() - 1
    return _rolling_skew(base, 5)

def supv_192_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 106 support violation distribution over 21d to detect tail risk or exhaustion.
    """
    base = close / low.rolling(60).min() - 1
    return _rolling_skew(base, 21)

def supv_193_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 106 support violation distribution over 63d to detect tail risk or exhaustion.
    """
    base = close / low.rolling(60).min() - 1
    return _rolling_skew(base, 63)

def supv_194_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 106 support violation distribution over 126d to detect tail risk or exhaustion.
    """
    base = close / low.rolling(60).min() - 1
    return _rolling_skew(base, 126)

def supv_195_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 106 support violation distribution over 252d to detect tail risk or exhaustion.
    """
    base = close / low.rolling(60).min() - 1
    return _rolling_skew(base, 252)

def supv_196_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 106 support violation over 5d to capture explosive breakdown or reversal points.
    """
    base = close / low.rolling(60).min() - 1
    return _rolling_kurt(base, 5)

def supv_197_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 106 support violation over 21d to capture explosive breakdown or reversal points.
    """
    base = close / low.rolling(60).min() - 1
    return _rolling_kurt(base, 21)

def supv_198_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 106 support violation over 63d to capture explosive breakdown or reversal points.
    """
    base = close / low.rolling(60).min() - 1
    return _rolling_kurt(base, 63)

def supv_199_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 106 support violation over 126d to capture explosive breakdown or reversal points.
    """
    base = close / low.rolling(60).min() - 1
    return _rolling_kurt(base, 126)

def supv_200_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 106 support violation over 252d to capture explosive breakdown or reversal points.
    """
    base = close / low.rolling(60).min() - 1
    return _rolling_kurt(base, 252)

def supv_201_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 106 support violation for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = close / low.rolling(60).min() - 1
    return _safe_div(base, _rolling_std(base, 5))

def supv_202_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 106 support violation for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = close / low.rolling(60).min() - 1
    return _safe_div(base, _rolling_std(base, 21))

def supv_203_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 106 support violation for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = close / low.rolling(60).min() - 1
    return _safe_div(base, _rolling_std(base, 63))

def supv_204_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 106 support violation for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = close / low.rolling(60).min() - 1
    return _safe_div(base, _rolling_std(base, 126))

def supv_205_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 106 support violation for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = close / low.rolling(60).min() - 1
    return _safe_div(base, _rolling_std(base, 252))

def supv_206_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 106 support violation over 5d to stabilize variance and capture exponential shifts.
    """
    base = close / low.rolling(60).min() - 1
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def supv_207_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 106 support violation over 21d to stabilize variance and capture exponential shifts.
    """
    base = close / low.rolling(60).min() - 1
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def supv_208_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 106 support violation over 63d to stabilize variance and capture exponential shifts.
    """
    base = close / low.rolling(60).min() - 1
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def supv_209_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 106 support violation over 126d to stabilize variance and capture exponential shifts.
    """
    base = close / low.rolling(60).min() - 1
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def supv_210_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 106 support violation over 252d to stabilize variance and capture exponential shifts.
    """
    base = close / low.rolling(60).min() - 1
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def supv_211_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 106 support violation over a 5d horizon to identify extreme regimes.
    """
    base = close / low.rolling(70).min() - 1
    return _rolling_mean(base, 5)

def supv_212_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 106 support violation over a 21d horizon to identify extreme regimes.
    """
    base = close / low.rolling(70).min() - 1
    return _rolling_mean(base, 21)

def supv_213_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 106 support violation over a 63d horizon to identify extreme regimes.
    """
    base = close / low.rolling(70).min() - 1
    return _rolling_mean(base, 63)

def supv_214_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 106 support violation over a 126d horizon to identify extreme regimes.
    """
    base = close / low.rolling(70).min() - 1
    return _rolling_mean(base, 126)

def supv_215_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 106 support violation over a 252d horizon to identify extreme regimes.
    """
    base = close / low.rolling(70).min() - 1
    return _rolling_mean(base, 252)

def supv_216_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 106 support violation by measuring deviations from the 5d mean.
    """
    base = close / low.rolling(70).min() - 1
    return _zscore_rolling(base, 5)

def supv_217_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 106 support violation by measuring deviations from the 21d mean.
    """
    base = close / low.rolling(70).min() - 1
    return _zscore_rolling(base, 21)

def supv_218_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 106 support violation by measuring deviations from the 63d mean.
    """
    base = close / low.rolling(70).min() - 1
    return _zscore_rolling(base, 63)

def supv_219_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 106 support violation by measuring deviations from the 126d mean.
    """
    base = close / low.rolling(70).min() - 1
    return _zscore_rolling(base, 126)

def supv_220_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 106 support violation by measuring deviations from the 252d mean.
    """
    base = close / low.rolling(70).min() - 1
    return _zscore_rolling(base, 252)

def supv_221_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 106 support violation to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = close / low.rolling(70).min() - 1
    return _rank_pct(base, 5)

def supv_222_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 106 support violation to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = close / low.rolling(70).min() - 1
    return _rank_pct(base, 21)

def supv_223_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 106 support violation to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = close / low.rolling(70).min() - 1
    return _rank_pct(base, 63)

def supv_224_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 106 support violation to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = close / low.rolling(70).min() - 1
    return _rank_pct(base, 126)

def supv_225_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 106 support violation to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = close / low.rolling(70).min() - 1
    return _rank_pct(base, 252)
