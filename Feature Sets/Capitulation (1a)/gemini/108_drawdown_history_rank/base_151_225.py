"""
108_108_drawdown_history_rank — Base Features 151-225
Domain: 108_drawdown_history_rank
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

def dhrk_151_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 108 drawdown history rank to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = (close / close.rolling(100).max() - 1)
    return _rank_pct(base, 5)

def dhrk_152_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 108 drawdown history rank to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = (close / close.rolling(100).max() - 1)
    return _rank_pct(base, 21)

def dhrk_153_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 108 drawdown history rank to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = (close / close.rolling(100).max() - 1)
    return _rank_pct(base, 63)

def dhrk_154_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 108 drawdown history rank to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = (close / close.rolling(100).max() - 1)
    return _rank_pct(base, 126)

def dhrk_155_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 108 drawdown history rank to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = (close / close.rolling(100).max() - 1)
    return _rank_pct(base, 252)

def dhrk_156_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 108 drawdown history rank distribution over 5d to detect tail risk or exhaustion.
    """
    base = (close / close.rolling(100).max() - 1)
    return _rolling_skew(base, 5)

def dhrk_157_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 108 drawdown history rank distribution over 21d to detect tail risk or exhaustion.
    """
    base = (close / close.rolling(100).max() - 1)
    return _rolling_skew(base, 21)

def dhrk_158_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 108 drawdown history rank distribution over 63d to detect tail risk or exhaustion.
    """
    base = (close / close.rolling(100).max() - 1)
    return _rolling_skew(base, 63)

def dhrk_159_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 108 drawdown history rank distribution over 126d to detect tail risk or exhaustion.
    """
    base = (close / close.rolling(100).max() - 1)
    return _rolling_skew(base, 126)

def dhrk_160_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 108 drawdown history rank distribution over 252d to detect tail risk or exhaustion.
    """
    base = (close / close.rolling(100).max() - 1)
    return _rolling_skew(base, 252)

def dhrk_161_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 108 drawdown history rank over 5d to capture explosive breakdown or reversal points.
    """
    base = (close / close.rolling(100).max() - 1)
    return _rolling_kurt(base, 5)

def dhrk_162_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 108 drawdown history rank over 21d to capture explosive breakdown or reversal points.
    """
    base = (close / close.rolling(100).max() - 1)
    return _rolling_kurt(base, 21)

def dhrk_163_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 108 drawdown history rank over 63d to capture explosive breakdown or reversal points.
    """
    base = (close / close.rolling(100).max() - 1)
    return _rolling_kurt(base, 63)

def dhrk_164_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 108 drawdown history rank over 126d to capture explosive breakdown or reversal points.
    """
    base = (close / close.rolling(100).max() - 1)
    return _rolling_kurt(base, 126)

def dhrk_165_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 108 drawdown history rank over 252d to capture explosive breakdown or reversal points.
    """
    base = (close / close.rolling(100).max() - 1)
    return _rolling_kurt(base, 252)

def dhrk_166_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 108 drawdown history rank for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = (close / close.rolling(100).max() - 1)
    return _safe_div(base, _rolling_std(base, 5))

def dhrk_167_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 108 drawdown history rank for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = (close / close.rolling(100).max() - 1)
    return _safe_div(base, _rolling_std(base, 21))

def dhrk_168_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 108 drawdown history rank for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = (close / close.rolling(100).max() - 1)
    return _safe_div(base, _rolling_std(base, 63))

def dhrk_169_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 108 drawdown history rank for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = (close / close.rolling(100).max() - 1)
    return _safe_div(base, _rolling_std(base, 126))

def dhrk_170_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 108 drawdown history rank for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = (close / close.rolling(100).max() - 1)
    return _safe_div(base, _rolling_std(base, 252))

def dhrk_171_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 108 drawdown history rank over 5d to stabilize variance and capture exponential shifts.
    """
    base = (close / close.rolling(100).max() - 1)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def dhrk_172_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 108 drawdown history rank over 21d to stabilize variance and capture exponential shifts.
    """
    base = (close / close.rolling(100).max() - 1)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def dhrk_173_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 108 drawdown history rank over 63d to stabilize variance and capture exponential shifts.
    """
    base = (close / close.rolling(100).max() - 1)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def dhrk_174_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 108 drawdown history rank over 126d to stabilize variance and capture exponential shifts.
    """
    base = (close / close.rolling(100).max() - 1)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def dhrk_175_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 108 drawdown history rank over 252d to stabilize variance and capture exponential shifts.
    """
    base = (close / close.rolling(100).max() - 1)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def dhrk_176_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 108 drawdown history rank over a 5d horizon to identify extreme regimes.
    """
    base = (close / close.rolling(120).max() - 1)
    return _rolling_mean(base, 5)

def dhrk_177_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 108 drawdown history rank over a 21d horizon to identify extreme regimes.
    """
    base = (close / close.rolling(120).max() - 1)
    return _rolling_mean(base, 21)

def dhrk_178_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 108 drawdown history rank over a 63d horizon to identify extreme regimes.
    """
    base = (close / close.rolling(120).max() - 1)
    return _rolling_mean(base, 63)

def dhrk_179_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 108 drawdown history rank over a 126d horizon to identify extreme regimes.
    """
    base = (close / close.rolling(120).max() - 1)
    return _rolling_mean(base, 126)

def dhrk_180_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 108 drawdown history rank over a 252d horizon to identify extreme regimes.
    """
    base = (close / close.rolling(120).max() - 1)
    return _rolling_mean(base, 252)

def dhrk_181_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 108 drawdown history rank by measuring deviations from the 5d mean.
    """
    base = (close / close.rolling(120).max() - 1)
    return _zscore_rolling(base, 5)

def dhrk_182_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 108 drawdown history rank by measuring deviations from the 21d mean.
    """
    base = (close / close.rolling(120).max() - 1)
    return _zscore_rolling(base, 21)

def dhrk_183_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 108 drawdown history rank by measuring deviations from the 63d mean.
    """
    base = (close / close.rolling(120).max() - 1)
    return _zscore_rolling(base, 63)

def dhrk_184_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 108 drawdown history rank by measuring deviations from the 126d mean.
    """
    base = (close / close.rolling(120).max() - 1)
    return _zscore_rolling(base, 126)

def dhrk_185_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 108 drawdown history rank by measuring deviations from the 252d mean.
    """
    base = (close / close.rolling(120).max() - 1)
    return _zscore_rolling(base, 252)

def dhrk_186_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 108 drawdown history rank to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = (close / close.rolling(120).max() - 1)
    return _rank_pct(base, 5)

def dhrk_187_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 108 drawdown history rank to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = (close / close.rolling(120).max() - 1)
    return _rank_pct(base, 21)

def dhrk_188_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 108 drawdown history rank to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = (close / close.rolling(120).max() - 1)
    return _rank_pct(base, 63)

def dhrk_189_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 108 drawdown history rank to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = (close / close.rolling(120).max() - 1)
    return _rank_pct(base, 126)

def dhrk_190_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 108 drawdown history rank to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = (close / close.rolling(120).max() - 1)
    return _rank_pct(base, 252)

def dhrk_191_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 108 drawdown history rank distribution over 5d to detect tail risk or exhaustion.
    """
    base = (close / close.rolling(120).max() - 1)
    return _rolling_skew(base, 5)

def dhrk_192_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 108 drawdown history rank distribution over 21d to detect tail risk or exhaustion.
    """
    base = (close / close.rolling(120).max() - 1)
    return _rolling_skew(base, 21)

def dhrk_193_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 108 drawdown history rank distribution over 63d to detect tail risk or exhaustion.
    """
    base = (close / close.rolling(120).max() - 1)
    return _rolling_skew(base, 63)

def dhrk_194_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 108 drawdown history rank distribution over 126d to detect tail risk or exhaustion.
    """
    base = (close / close.rolling(120).max() - 1)
    return _rolling_skew(base, 126)

def dhrk_195_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 108 drawdown history rank distribution over 252d to detect tail risk or exhaustion.
    """
    base = (close / close.rolling(120).max() - 1)
    return _rolling_skew(base, 252)

def dhrk_196_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 108 drawdown history rank over 5d to capture explosive breakdown or reversal points.
    """
    base = (close / close.rolling(120).max() - 1)
    return _rolling_kurt(base, 5)

def dhrk_197_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 108 drawdown history rank over 21d to capture explosive breakdown or reversal points.
    """
    base = (close / close.rolling(120).max() - 1)
    return _rolling_kurt(base, 21)

def dhrk_198_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 108 drawdown history rank over 63d to capture explosive breakdown or reversal points.
    """
    base = (close / close.rolling(120).max() - 1)
    return _rolling_kurt(base, 63)

def dhrk_199_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 108 drawdown history rank over 126d to capture explosive breakdown or reversal points.
    """
    base = (close / close.rolling(120).max() - 1)
    return _rolling_kurt(base, 126)

def dhrk_200_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 108 drawdown history rank over 252d to capture explosive breakdown or reversal points.
    """
    base = (close / close.rolling(120).max() - 1)
    return _rolling_kurt(base, 252)

def dhrk_201_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 108 drawdown history rank for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = (close / close.rolling(120).max() - 1)
    return _safe_div(base, _rolling_std(base, 5))

def dhrk_202_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 108 drawdown history rank for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = (close / close.rolling(120).max() - 1)
    return _safe_div(base, _rolling_std(base, 21))

def dhrk_203_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 108 drawdown history rank for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = (close / close.rolling(120).max() - 1)
    return _safe_div(base, _rolling_std(base, 63))

def dhrk_204_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 108 drawdown history rank for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = (close / close.rolling(120).max() - 1)
    return _safe_div(base, _rolling_std(base, 126))

def dhrk_205_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 108 drawdown history rank for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = (close / close.rolling(120).max() - 1)
    return _safe_div(base, _rolling_std(base, 252))

def dhrk_206_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 108 drawdown history rank over 5d to stabilize variance and capture exponential shifts.
    """
    base = (close / close.rolling(120).max() - 1)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def dhrk_207_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 108 drawdown history rank over 21d to stabilize variance and capture exponential shifts.
    """
    base = (close / close.rolling(120).max() - 1)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def dhrk_208_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 108 drawdown history rank over 63d to stabilize variance and capture exponential shifts.
    """
    base = (close / close.rolling(120).max() - 1)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def dhrk_209_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 108 drawdown history rank over 126d to stabilize variance and capture exponential shifts.
    """
    base = (close / close.rolling(120).max() - 1)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def dhrk_210_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 108 drawdown history rank over 252d to stabilize variance and capture exponential shifts.
    """
    base = (close / close.rolling(120).max() - 1)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def dhrk_211_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 108 drawdown history rank over a 5d horizon to identify extreme regimes.
    """
    base = (close / close.rolling(140).max() - 1)
    return _rolling_mean(base, 5)

def dhrk_212_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 108 drawdown history rank over a 21d horizon to identify extreme regimes.
    """
    base = (close / close.rolling(140).max() - 1)
    return _rolling_mean(base, 21)

def dhrk_213_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 108 drawdown history rank over a 63d horizon to identify extreme regimes.
    """
    base = (close / close.rolling(140).max() - 1)
    return _rolling_mean(base, 63)

def dhrk_214_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 108 drawdown history rank over a 126d horizon to identify extreme regimes.
    """
    base = (close / close.rolling(140).max() - 1)
    return _rolling_mean(base, 126)

def dhrk_215_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 108 drawdown history rank over a 252d horizon to identify extreme regimes.
    """
    base = (close / close.rolling(140).max() - 1)
    return _rolling_mean(base, 252)

def dhrk_216_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 108 drawdown history rank by measuring deviations from the 5d mean.
    """
    base = (close / close.rolling(140).max() - 1)
    return _zscore_rolling(base, 5)

def dhrk_217_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 108 drawdown history rank by measuring deviations from the 21d mean.
    """
    base = (close / close.rolling(140).max() - 1)
    return _zscore_rolling(base, 21)

def dhrk_218_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 108 drawdown history rank by measuring deviations from the 63d mean.
    """
    base = (close / close.rolling(140).max() - 1)
    return _zscore_rolling(base, 63)

def dhrk_219_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 108 drawdown history rank by measuring deviations from the 126d mean.
    """
    base = (close / close.rolling(140).max() - 1)
    return _zscore_rolling(base, 126)

def dhrk_220_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 108 drawdown history rank by measuring deviations from the 252d mean.
    """
    base = (close / close.rolling(140).max() - 1)
    return _zscore_rolling(base, 252)

def dhrk_221_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 108 drawdown history rank to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = (close / close.rolling(140).max() - 1)
    return _rank_pct(base, 5)

def dhrk_222_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 108 drawdown history rank to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = (close / close.rolling(140).max() - 1)
    return _rank_pct(base, 21)

def dhrk_223_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 108 drawdown history rank to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = (close / close.rolling(140).max() - 1)
    return _rank_pct(base, 63)

def dhrk_224_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 108 drawdown history rank to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = (close / close.rolling(140).max() - 1)
    return _rank_pct(base, 126)

def dhrk_225_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 108 drawdown history rank to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = (close / close.rolling(140).max() - 1)
    return _rank_pct(base, 252)
