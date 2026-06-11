"""
118_118_drawdown_recovery_asymmetry — Base Features 151-225
Domain: 118_drawdown_recovery_asymmetry
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

def dras_151_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 118 drawdown recovery asymmetry to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(50).skew()
    return _rank_pct(base, 5)

def dras_152_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 118 drawdown recovery asymmetry to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(50).skew()
    return _rank_pct(base, 21)

def dras_153_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 118 drawdown recovery asymmetry to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(50).skew()
    return _rank_pct(base, 63)

def dras_154_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 118 drawdown recovery asymmetry to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(50).skew()
    return _rank_pct(base, 126)

def dras_155_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 118 drawdown recovery asymmetry to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(50).skew()
    return _rank_pct(base, 252)

def dras_156_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 118 drawdown recovery asymmetry distribution over 5d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(50).skew()
    return _rolling_skew(base, 5)

def dras_157_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 118 drawdown recovery asymmetry distribution over 21d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(50).skew()
    return _rolling_skew(base, 21)

def dras_158_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 118 drawdown recovery asymmetry distribution over 63d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(50).skew()
    return _rolling_skew(base, 63)

def dras_159_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 118 drawdown recovery asymmetry distribution over 126d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(50).skew()
    return _rolling_skew(base, 126)

def dras_160_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 118 drawdown recovery asymmetry distribution over 252d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(50).skew()
    return _rolling_skew(base, 252)

def dras_161_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 118 drawdown recovery asymmetry over 5d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(50).skew()
    return _rolling_kurt(base, 5)

def dras_162_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 118 drawdown recovery asymmetry over 21d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(50).skew()
    return _rolling_kurt(base, 21)

def dras_163_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 118 drawdown recovery asymmetry over 63d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(50).skew()
    return _rolling_kurt(base, 63)

def dras_164_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 118 drawdown recovery asymmetry over 126d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(50).skew()
    return _rolling_kurt(base, 126)

def dras_165_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 118 drawdown recovery asymmetry over 252d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(50).skew()
    return _rolling_kurt(base, 252)

def dras_166_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 118 drawdown recovery asymmetry for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(50).skew()
    return _safe_div(base, _rolling_std(base, 5))

def dras_167_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 118 drawdown recovery asymmetry for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(50).skew()
    return _safe_div(base, _rolling_std(base, 21))

def dras_168_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 118 drawdown recovery asymmetry for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(50).skew()
    return _safe_div(base, _rolling_std(base, 63))

def dras_169_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 118 drawdown recovery asymmetry for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(50).skew()
    return _safe_div(base, _rolling_std(base, 126))

def dras_170_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 118 drawdown recovery asymmetry for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(50).skew()
    return _safe_div(base, _rolling_std(base, 252))

def dras_171_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 118 drawdown recovery asymmetry over 5d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(50).skew()
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def dras_172_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 118 drawdown recovery asymmetry over 21d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(50).skew()
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def dras_173_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 118 drawdown recovery asymmetry over 63d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(50).skew()
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def dras_174_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 118 drawdown recovery asymmetry over 126d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(50).skew()
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def dras_175_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 118 drawdown recovery asymmetry over 252d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(50).skew()
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def dras_176_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 118 drawdown recovery asymmetry over a 5d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(60).skew()
    return _rolling_mean(base, 5)

def dras_177_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 118 drawdown recovery asymmetry over a 21d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(60).skew()
    return _rolling_mean(base, 21)

def dras_178_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 118 drawdown recovery asymmetry over a 63d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(60).skew()
    return _rolling_mean(base, 63)

def dras_179_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 118 drawdown recovery asymmetry over a 126d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(60).skew()
    return _rolling_mean(base, 126)

def dras_180_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 118 drawdown recovery asymmetry over a 252d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(60).skew()
    return _rolling_mean(base, 252)

def dras_181_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 118 drawdown recovery asymmetry by measuring deviations from the 5d mean.
    """
    base = close.pct_change().rolling(60).skew()
    return _zscore_rolling(base, 5)

def dras_182_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 118 drawdown recovery asymmetry by measuring deviations from the 21d mean.
    """
    base = close.pct_change().rolling(60).skew()
    return _zscore_rolling(base, 21)

def dras_183_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 118 drawdown recovery asymmetry by measuring deviations from the 63d mean.
    """
    base = close.pct_change().rolling(60).skew()
    return _zscore_rolling(base, 63)

def dras_184_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 118 drawdown recovery asymmetry by measuring deviations from the 126d mean.
    """
    base = close.pct_change().rolling(60).skew()
    return _zscore_rolling(base, 126)

def dras_185_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 118 drawdown recovery asymmetry by measuring deviations from the 252d mean.
    """
    base = close.pct_change().rolling(60).skew()
    return _zscore_rolling(base, 252)

def dras_186_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 118 drawdown recovery asymmetry to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(60).skew()
    return _rank_pct(base, 5)

def dras_187_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 118 drawdown recovery asymmetry to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(60).skew()
    return _rank_pct(base, 21)

def dras_188_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 118 drawdown recovery asymmetry to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(60).skew()
    return _rank_pct(base, 63)

def dras_189_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 118 drawdown recovery asymmetry to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(60).skew()
    return _rank_pct(base, 126)

def dras_190_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 118 drawdown recovery asymmetry to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(60).skew()
    return _rank_pct(base, 252)

def dras_191_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 118 drawdown recovery asymmetry distribution over 5d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(60).skew()
    return _rolling_skew(base, 5)

def dras_192_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 118 drawdown recovery asymmetry distribution over 21d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(60).skew()
    return _rolling_skew(base, 21)

def dras_193_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 118 drawdown recovery asymmetry distribution over 63d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(60).skew()
    return _rolling_skew(base, 63)

def dras_194_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 118 drawdown recovery asymmetry distribution over 126d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(60).skew()
    return _rolling_skew(base, 126)

def dras_195_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 118 drawdown recovery asymmetry distribution over 252d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(60).skew()
    return _rolling_skew(base, 252)

def dras_196_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 118 drawdown recovery asymmetry over 5d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(60).skew()
    return _rolling_kurt(base, 5)

def dras_197_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 118 drawdown recovery asymmetry over 21d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(60).skew()
    return _rolling_kurt(base, 21)

def dras_198_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 118 drawdown recovery asymmetry over 63d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(60).skew()
    return _rolling_kurt(base, 63)

def dras_199_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 118 drawdown recovery asymmetry over 126d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(60).skew()
    return _rolling_kurt(base, 126)

def dras_200_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 118 drawdown recovery asymmetry over 252d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(60).skew()
    return _rolling_kurt(base, 252)

def dras_201_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 118 drawdown recovery asymmetry for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(60).skew()
    return _safe_div(base, _rolling_std(base, 5))

def dras_202_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 118 drawdown recovery asymmetry for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(60).skew()
    return _safe_div(base, _rolling_std(base, 21))

def dras_203_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 118 drawdown recovery asymmetry for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(60).skew()
    return _safe_div(base, _rolling_std(base, 63))

def dras_204_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 118 drawdown recovery asymmetry for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(60).skew()
    return _safe_div(base, _rolling_std(base, 126))

def dras_205_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 118 drawdown recovery asymmetry for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(60).skew()
    return _safe_div(base, _rolling_std(base, 252))

def dras_206_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 118 drawdown recovery asymmetry over 5d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(60).skew()
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def dras_207_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 118 drawdown recovery asymmetry over 21d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(60).skew()
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def dras_208_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 118 drawdown recovery asymmetry over 63d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(60).skew()
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def dras_209_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 118 drawdown recovery asymmetry over 126d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(60).skew()
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def dras_210_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 118 drawdown recovery asymmetry over 252d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(60).skew()
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def dras_211_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 118 drawdown recovery asymmetry over a 5d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(70).skew()
    return _rolling_mean(base, 5)

def dras_212_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 118 drawdown recovery asymmetry over a 21d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(70).skew()
    return _rolling_mean(base, 21)

def dras_213_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 118 drawdown recovery asymmetry over a 63d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(70).skew()
    return _rolling_mean(base, 63)

def dras_214_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 118 drawdown recovery asymmetry over a 126d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(70).skew()
    return _rolling_mean(base, 126)

def dras_215_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 118 drawdown recovery asymmetry over a 252d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(70).skew()
    return _rolling_mean(base, 252)

def dras_216_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 118 drawdown recovery asymmetry by measuring deviations from the 5d mean.
    """
    base = close.pct_change().rolling(70).skew()
    return _zscore_rolling(base, 5)

def dras_217_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 118 drawdown recovery asymmetry by measuring deviations from the 21d mean.
    """
    base = close.pct_change().rolling(70).skew()
    return _zscore_rolling(base, 21)

def dras_218_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 118 drawdown recovery asymmetry by measuring deviations from the 63d mean.
    """
    base = close.pct_change().rolling(70).skew()
    return _zscore_rolling(base, 63)

def dras_219_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 118 drawdown recovery asymmetry by measuring deviations from the 126d mean.
    """
    base = close.pct_change().rolling(70).skew()
    return _zscore_rolling(base, 126)

def dras_220_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 118 drawdown recovery asymmetry by measuring deviations from the 252d mean.
    """
    base = close.pct_change().rolling(70).skew()
    return _zscore_rolling(base, 252)

def dras_221_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 118 drawdown recovery asymmetry to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(70).skew()
    return _rank_pct(base, 5)

def dras_222_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 118 drawdown recovery asymmetry to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(70).skew()
    return _rank_pct(base, 21)

def dras_223_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 118 drawdown recovery asymmetry to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(70).skew()
    return _rank_pct(base, 63)

def dras_224_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 118 drawdown recovery asymmetry to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(70).skew()
    return _rank_pct(base, 126)

def dras_225_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 118 drawdown recovery asymmetry to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(70).skew()
    return _rank_pct(base, 252)
