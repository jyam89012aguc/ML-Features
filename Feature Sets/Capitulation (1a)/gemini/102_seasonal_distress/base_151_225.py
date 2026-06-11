"""
102_102_seasonal_distress — Base Features 151-225
Domain: 102_seasonal_distress
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

def seas_151_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 102 seasonal distress to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = close.pct_change(25)
    return _rank_pct(base, 5)

def seas_152_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 102 seasonal distress to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = close.pct_change(25)
    return _rank_pct(base, 21)

def seas_153_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 102 seasonal distress to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = close.pct_change(25)
    return _rank_pct(base, 63)

def seas_154_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 102 seasonal distress to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = close.pct_change(25)
    return _rank_pct(base, 126)

def seas_155_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 102 seasonal distress to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = close.pct_change(25)
    return _rank_pct(base, 252)

def seas_156_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 102 seasonal distress distribution over 5d to detect tail risk or exhaustion.
    """
    base = close.pct_change(25)
    return _rolling_skew(base, 5)

def seas_157_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 102 seasonal distress distribution over 21d to detect tail risk or exhaustion.
    """
    base = close.pct_change(25)
    return _rolling_skew(base, 21)

def seas_158_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 102 seasonal distress distribution over 63d to detect tail risk or exhaustion.
    """
    base = close.pct_change(25)
    return _rolling_skew(base, 63)

def seas_159_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 102 seasonal distress distribution over 126d to detect tail risk or exhaustion.
    """
    base = close.pct_change(25)
    return _rolling_skew(base, 126)

def seas_160_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 102 seasonal distress distribution over 252d to detect tail risk or exhaustion.
    """
    base = close.pct_change(25)
    return _rolling_skew(base, 252)

def seas_161_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 102 seasonal distress over 5d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change(25)
    return _rolling_kurt(base, 5)

def seas_162_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 102 seasonal distress over 21d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change(25)
    return _rolling_kurt(base, 21)

def seas_163_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 102 seasonal distress over 63d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change(25)
    return _rolling_kurt(base, 63)

def seas_164_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 102 seasonal distress over 126d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change(25)
    return _rolling_kurt(base, 126)

def seas_165_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 102 seasonal distress over 252d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change(25)
    return _rolling_kurt(base, 252)

def seas_166_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 102 seasonal distress for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change(25)
    return _safe_div(base, _rolling_std(base, 5))

def seas_167_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 102 seasonal distress for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change(25)
    return _safe_div(base, _rolling_std(base, 21))

def seas_168_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 102 seasonal distress for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change(25)
    return _safe_div(base, _rolling_std(base, 63))

def seas_169_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 102 seasonal distress for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change(25)
    return _safe_div(base, _rolling_std(base, 126))

def seas_170_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 102 seasonal distress for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change(25)
    return _safe_div(base, _rolling_std(base, 252))

def seas_171_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 102 seasonal distress over 5d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change(25)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def seas_172_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 102 seasonal distress over 21d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change(25)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def seas_173_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 102 seasonal distress over 63d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change(25)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def seas_174_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 102 seasonal distress over 126d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change(25)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def seas_175_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 102 seasonal distress over 252d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change(25)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def seas_176_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 102 seasonal distress over a 5d horizon to identify extreme regimes.
    """
    base = close.pct_change(30)
    return _rolling_mean(base, 5)

def seas_177_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 102 seasonal distress over a 21d horizon to identify extreme regimes.
    """
    base = close.pct_change(30)
    return _rolling_mean(base, 21)

def seas_178_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 102 seasonal distress over a 63d horizon to identify extreme regimes.
    """
    base = close.pct_change(30)
    return _rolling_mean(base, 63)

def seas_179_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 102 seasonal distress over a 126d horizon to identify extreme regimes.
    """
    base = close.pct_change(30)
    return _rolling_mean(base, 126)

def seas_180_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 102 seasonal distress over a 252d horizon to identify extreme regimes.
    """
    base = close.pct_change(30)
    return _rolling_mean(base, 252)

def seas_181_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 102 seasonal distress by measuring deviations from the 5d mean.
    """
    base = close.pct_change(30)
    return _zscore_rolling(base, 5)

def seas_182_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 102 seasonal distress by measuring deviations from the 21d mean.
    """
    base = close.pct_change(30)
    return _zscore_rolling(base, 21)

def seas_183_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 102 seasonal distress by measuring deviations from the 63d mean.
    """
    base = close.pct_change(30)
    return _zscore_rolling(base, 63)

def seas_184_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 102 seasonal distress by measuring deviations from the 126d mean.
    """
    base = close.pct_change(30)
    return _zscore_rolling(base, 126)

def seas_185_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 102 seasonal distress by measuring deviations from the 252d mean.
    """
    base = close.pct_change(30)
    return _zscore_rolling(base, 252)

def seas_186_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 102 seasonal distress to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = close.pct_change(30)
    return _rank_pct(base, 5)

def seas_187_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 102 seasonal distress to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = close.pct_change(30)
    return _rank_pct(base, 21)

def seas_188_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 102 seasonal distress to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = close.pct_change(30)
    return _rank_pct(base, 63)

def seas_189_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 102 seasonal distress to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = close.pct_change(30)
    return _rank_pct(base, 126)

def seas_190_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 102 seasonal distress to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = close.pct_change(30)
    return _rank_pct(base, 252)

def seas_191_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 102 seasonal distress distribution over 5d to detect tail risk or exhaustion.
    """
    base = close.pct_change(30)
    return _rolling_skew(base, 5)

def seas_192_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 102 seasonal distress distribution over 21d to detect tail risk or exhaustion.
    """
    base = close.pct_change(30)
    return _rolling_skew(base, 21)

def seas_193_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 102 seasonal distress distribution over 63d to detect tail risk or exhaustion.
    """
    base = close.pct_change(30)
    return _rolling_skew(base, 63)

def seas_194_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 102 seasonal distress distribution over 126d to detect tail risk or exhaustion.
    """
    base = close.pct_change(30)
    return _rolling_skew(base, 126)

def seas_195_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 102 seasonal distress distribution over 252d to detect tail risk or exhaustion.
    """
    base = close.pct_change(30)
    return _rolling_skew(base, 252)

def seas_196_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 102 seasonal distress over 5d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change(30)
    return _rolling_kurt(base, 5)

def seas_197_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 102 seasonal distress over 21d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change(30)
    return _rolling_kurt(base, 21)

def seas_198_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 102 seasonal distress over 63d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change(30)
    return _rolling_kurt(base, 63)

def seas_199_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 102 seasonal distress over 126d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change(30)
    return _rolling_kurt(base, 126)

def seas_200_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 102 seasonal distress over 252d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change(30)
    return _rolling_kurt(base, 252)

def seas_201_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 102 seasonal distress for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change(30)
    return _safe_div(base, _rolling_std(base, 5))

def seas_202_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 102 seasonal distress for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change(30)
    return _safe_div(base, _rolling_std(base, 21))

def seas_203_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 102 seasonal distress for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change(30)
    return _safe_div(base, _rolling_std(base, 63))

def seas_204_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 102 seasonal distress for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change(30)
    return _safe_div(base, _rolling_std(base, 126))

def seas_205_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 102 seasonal distress for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change(30)
    return _safe_div(base, _rolling_std(base, 252))

def seas_206_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 102 seasonal distress over 5d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change(30)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def seas_207_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 102 seasonal distress over 21d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change(30)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def seas_208_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 102 seasonal distress over 63d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change(30)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def seas_209_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 102 seasonal distress over 126d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change(30)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def seas_210_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 102 seasonal distress over 252d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change(30)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def seas_211_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 102 seasonal distress over a 5d horizon to identify extreme regimes.
    """
    base = close.pct_change(35)
    return _rolling_mean(base, 5)

def seas_212_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 102 seasonal distress over a 21d horizon to identify extreme regimes.
    """
    base = close.pct_change(35)
    return _rolling_mean(base, 21)

def seas_213_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 102 seasonal distress over a 63d horizon to identify extreme regimes.
    """
    base = close.pct_change(35)
    return _rolling_mean(base, 63)

def seas_214_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 102 seasonal distress over a 126d horizon to identify extreme regimes.
    """
    base = close.pct_change(35)
    return _rolling_mean(base, 126)

def seas_215_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 102 seasonal distress over a 252d horizon to identify extreme regimes.
    """
    base = close.pct_change(35)
    return _rolling_mean(base, 252)

def seas_216_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 102 seasonal distress by measuring deviations from the 5d mean.
    """
    base = close.pct_change(35)
    return _zscore_rolling(base, 5)

def seas_217_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 102 seasonal distress by measuring deviations from the 21d mean.
    """
    base = close.pct_change(35)
    return _zscore_rolling(base, 21)

def seas_218_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 102 seasonal distress by measuring deviations from the 63d mean.
    """
    base = close.pct_change(35)
    return _zscore_rolling(base, 63)

def seas_219_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 102 seasonal distress by measuring deviations from the 126d mean.
    """
    base = close.pct_change(35)
    return _zscore_rolling(base, 126)

def seas_220_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 102 seasonal distress by measuring deviations from the 252d mean.
    """
    base = close.pct_change(35)
    return _zscore_rolling(base, 252)

def seas_221_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 102 seasonal distress to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = close.pct_change(35)
    return _rank_pct(base, 5)

def seas_222_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 102 seasonal distress to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = close.pct_change(35)
    return _rank_pct(base, 21)

def seas_223_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 102 seasonal distress to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = close.pct_change(35)
    return _rank_pct(base, 63)

def seas_224_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 102 seasonal distress to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = close.pct_change(35)
    return _rank_pct(base, 126)

def seas_225_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 102 seasonal distress to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = close.pct_change(35)
    return _rank_pct(base, 252)
