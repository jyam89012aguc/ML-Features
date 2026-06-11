"""
110_110_tail_risk_evt — Base Features 151-225
Domain: 110_tail_risk_evt
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

def trev_151_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 110 tail risk evt to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(250).quantile(0.01)
    return _rank_pct(base, 5)

def trev_152_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 110 tail risk evt to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(250).quantile(0.01)
    return _rank_pct(base, 21)

def trev_153_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 110 tail risk evt to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(250).quantile(0.01)
    return _rank_pct(base, 63)

def trev_154_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 110 tail risk evt to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(250).quantile(0.01)
    return _rank_pct(base, 126)

def trev_155_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 110 tail risk evt to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(250).quantile(0.01)
    return _rank_pct(base, 252)

def trev_156_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 110 tail risk evt distribution over 5d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(250).quantile(0.01)
    return _rolling_skew(base, 5)

def trev_157_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 110 tail risk evt distribution over 21d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(250).quantile(0.01)
    return _rolling_skew(base, 21)

def trev_158_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 110 tail risk evt distribution over 63d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(250).quantile(0.01)
    return _rolling_skew(base, 63)

def trev_159_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 110 tail risk evt distribution over 126d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(250).quantile(0.01)
    return _rolling_skew(base, 126)

def trev_160_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 110 tail risk evt distribution over 252d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(250).quantile(0.01)
    return _rolling_skew(base, 252)

def trev_161_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 110 tail risk evt over 5d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(250).quantile(0.01)
    return _rolling_kurt(base, 5)

def trev_162_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 110 tail risk evt over 21d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(250).quantile(0.01)
    return _rolling_kurt(base, 21)

def trev_163_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 110 tail risk evt over 63d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(250).quantile(0.01)
    return _rolling_kurt(base, 63)

def trev_164_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 110 tail risk evt over 126d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(250).quantile(0.01)
    return _rolling_kurt(base, 126)

def trev_165_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 110 tail risk evt over 252d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(250).quantile(0.01)
    return _rolling_kurt(base, 252)

def trev_166_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 110 tail risk evt for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(250).quantile(0.01)
    return _safe_div(base, _rolling_std(base, 5))

def trev_167_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 110 tail risk evt for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(250).quantile(0.01)
    return _safe_div(base, _rolling_std(base, 21))

def trev_168_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 110 tail risk evt for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(250).quantile(0.01)
    return _safe_div(base, _rolling_std(base, 63))

def trev_169_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 110 tail risk evt for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(250).quantile(0.01)
    return _safe_div(base, _rolling_std(base, 126))

def trev_170_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 110 tail risk evt for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(250).quantile(0.01)
    return _safe_div(base, _rolling_std(base, 252))

def trev_171_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 110 tail risk evt over 5d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(250).quantile(0.01)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def trev_172_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 110 tail risk evt over 21d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(250).quantile(0.01)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def trev_173_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 110 tail risk evt over 63d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(250).quantile(0.01)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def trev_174_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 110 tail risk evt over 126d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(250).quantile(0.01)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def trev_175_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 110 tail risk evt over 252d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(250).quantile(0.01)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def trev_176_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 110 tail risk evt over a 5d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(300).quantile(0.01)
    return _rolling_mean(base, 5)

def trev_177_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 110 tail risk evt over a 21d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(300).quantile(0.01)
    return _rolling_mean(base, 21)

def trev_178_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 110 tail risk evt over a 63d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(300).quantile(0.01)
    return _rolling_mean(base, 63)

def trev_179_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 110 tail risk evt over a 126d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(300).quantile(0.01)
    return _rolling_mean(base, 126)

def trev_180_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 110 tail risk evt over a 252d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(300).quantile(0.01)
    return _rolling_mean(base, 252)

def trev_181_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 110 tail risk evt by measuring deviations from the 5d mean.
    """
    base = close.pct_change().rolling(300).quantile(0.01)
    return _zscore_rolling(base, 5)

def trev_182_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 110 tail risk evt by measuring deviations from the 21d mean.
    """
    base = close.pct_change().rolling(300).quantile(0.01)
    return _zscore_rolling(base, 21)

def trev_183_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 110 tail risk evt by measuring deviations from the 63d mean.
    """
    base = close.pct_change().rolling(300).quantile(0.01)
    return _zscore_rolling(base, 63)

def trev_184_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 110 tail risk evt by measuring deviations from the 126d mean.
    """
    base = close.pct_change().rolling(300).quantile(0.01)
    return _zscore_rolling(base, 126)

def trev_185_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 110 tail risk evt by measuring deviations from the 252d mean.
    """
    base = close.pct_change().rolling(300).quantile(0.01)
    return _zscore_rolling(base, 252)

def trev_186_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 110 tail risk evt to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(300).quantile(0.01)
    return _rank_pct(base, 5)

def trev_187_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 110 tail risk evt to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(300).quantile(0.01)
    return _rank_pct(base, 21)

def trev_188_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 110 tail risk evt to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(300).quantile(0.01)
    return _rank_pct(base, 63)

def trev_189_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 110 tail risk evt to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(300).quantile(0.01)
    return _rank_pct(base, 126)

def trev_190_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 110 tail risk evt to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(300).quantile(0.01)
    return _rank_pct(base, 252)

def trev_191_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 110 tail risk evt distribution over 5d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(300).quantile(0.01)
    return _rolling_skew(base, 5)

def trev_192_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 110 tail risk evt distribution over 21d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(300).quantile(0.01)
    return _rolling_skew(base, 21)

def trev_193_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 110 tail risk evt distribution over 63d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(300).quantile(0.01)
    return _rolling_skew(base, 63)

def trev_194_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 110 tail risk evt distribution over 126d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(300).quantile(0.01)
    return _rolling_skew(base, 126)

def trev_195_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 110 tail risk evt distribution over 252d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(300).quantile(0.01)
    return _rolling_skew(base, 252)

def trev_196_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 110 tail risk evt over 5d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(300).quantile(0.01)
    return _rolling_kurt(base, 5)

def trev_197_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 110 tail risk evt over 21d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(300).quantile(0.01)
    return _rolling_kurt(base, 21)

def trev_198_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 110 tail risk evt over 63d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(300).quantile(0.01)
    return _rolling_kurt(base, 63)

def trev_199_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 110 tail risk evt over 126d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(300).quantile(0.01)
    return _rolling_kurt(base, 126)

def trev_200_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 110 tail risk evt over 252d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(300).quantile(0.01)
    return _rolling_kurt(base, 252)

def trev_201_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 110 tail risk evt for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(300).quantile(0.01)
    return _safe_div(base, _rolling_std(base, 5))

def trev_202_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 110 tail risk evt for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(300).quantile(0.01)
    return _safe_div(base, _rolling_std(base, 21))

def trev_203_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 110 tail risk evt for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(300).quantile(0.01)
    return _safe_div(base, _rolling_std(base, 63))

def trev_204_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 110 tail risk evt for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(300).quantile(0.01)
    return _safe_div(base, _rolling_std(base, 126))

def trev_205_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 110 tail risk evt for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(300).quantile(0.01)
    return _safe_div(base, _rolling_std(base, 252))

def trev_206_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 110 tail risk evt over 5d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(300).quantile(0.01)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def trev_207_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 110 tail risk evt over 21d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(300).quantile(0.01)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def trev_208_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 110 tail risk evt over 63d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(300).quantile(0.01)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def trev_209_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 110 tail risk evt over 126d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(300).quantile(0.01)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def trev_210_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 110 tail risk evt over 252d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(300).quantile(0.01)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def trev_211_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 110 tail risk evt over a 5d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(350).quantile(0.01)
    return _rolling_mean(base, 5)

def trev_212_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 110 tail risk evt over a 21d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(350).quantile(0.01)
    return _rolling_mean(base, 21)

def trev_213_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 110 tail risk evt over a 63d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(350).quantile(0.01)
    return _rolling_mean(base, 63)

def trev_214_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 110 tail risk evt over a 126d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(350).quantile(0.01)
    return _rolling_mean(base, 126)

def trev_215_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 110 tail risk evt over a 252d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(350).quantile(0.01)
    return _rolling_mean(base, 252)

def trev_216_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 110 tail risk evt by measuring deviations from the 5d mean.
    """
    base = close.pct_change().rolling(350).quantile(0.01)
    return _zscore_rolling(base, 5)

def trev_217_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 110 tail risk evt by measuring deviations from the 21d mean.
    """
    base = close.pct_change().rolling(350).quantile(0.01)
    return _zscore_rolling(base, 21)

def trev_218_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 110 tail risk evt by measuring deviations from the 63d mean.
    """
    base = close.pct_change().rolling(350).quantile(0.01)
    return _zscore_rolling(base, 63)

def trev_219_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 110 tail risk evt by measuring deviations from the 126d mean.
    """
    base = close.pct_change().rolling(350).quantile(0.01)
    return _zscore_rolling(base, 126)

def trev_220_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 110 tail risk evt by measuring deviations from the 252d mean.
    """
    base = close.pct_change().rolling(350).quantile(0.01)
    return _zscore_rolling(base, 252)

def trev_221_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 110 tail risk evt to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(350).quantile(0.01)
    return _rank_pct(base, 5)

def trev_222_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 110 tail risk evt to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(350).quantile(0.01)
    return _rank_pct(base, 21)

def trev_223_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 110 tail risk evt to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(350).quantile(0.01)
    return _rank_pct(base, 63)

def trev_224_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 110 tail risk evt to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(350).quantile(0.01)
    return _rank_pct(base, 126)

def trev_225_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 110 tail risk evt to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(350).quantile(0.01)
    return _rank_pct(base, 252)
