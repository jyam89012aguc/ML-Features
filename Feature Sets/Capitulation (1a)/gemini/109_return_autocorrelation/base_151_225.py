"""
109_109_return_autocorrelation — Base Features 151-225
Domain: 109_return_autocorrelation
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

def raut_151_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 109 return autocorrelation to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=5), raw=True)
    return _rank_pct(base, 5)

def raut_152_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 109 return autocorrelation to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=5), raw=True)
    return _rank_pct(base, 21)

def raut_153_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 109 return autocorrelation to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=5), raw=True)
    return _rank_pct(base, 63)

def raut_154_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 109 return autocorrelation to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=5), raw=True)
    return _rank_pct(base, 126)

def raut_155_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 109 return autocorrelation to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=5), raw=True)
    return _rank_pct(base, 252)

def raut_156_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 109 return autocorrelation distribution over 5d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=5), raw=True)
    return _rolling_skew(base, 5)

def raut_157_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 109 return autocorrelation distribution over 21d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=5), raw=True)
    return _rolling_skew(base, 21)

def raut_158_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 109 return autocorrelation distribution over 63d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=5), raw=True)
    return _rolling_skew(base, 63)

def raut_159_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 109 return autocorrelation distribution over 126d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=5), raw=True)
    return _rolling_skew(base, 126)

def raut_160_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 109 return autocorrelation distribution over 252d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=5), raw=True)
    return _rolling_skew(base, 252)

def raut_161_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 109 return autocorrelation over 5d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=5), raw=True)
    return _rolling_kurt(base, 5)

def raut_162_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 109 return autocorrelation over 21d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=5), raw=True)
    return _rolling_kurt(base, 21)

def raut_163_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 109 return autocorrelation over 63d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=5), raw=True)
    return _rolling_kurt(base, 63)

def raut_164_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 109 return autocorrelation over 126d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=5), raw=True)
    return _rolling_kurt(base, 126)

def raut_165_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 109 return autocorrelation over 252d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=5), raw=True)
    return _rolling_kurt(base, 252)

def raut_166_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 109 return autocorrelation for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=5), raw=True)
    return _safe_div(base, _rolling_std(base, 5))

def raut_167_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 109 return autocorrelation for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=5), raw=True)
    return _safe_div(base, _rolling_std(base, 21))

def raut_168_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 109 return autocorrelation for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=5), raw=True)
    return _safe_div(base, _rolling_std(base, 63))

def raut_169_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 109 return autocorrelation for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=5), raw=True)
    return _safe_div(base, _rolling_std(base, 126))

def raut_170_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 109 return autocorrelation for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=5), raw=True)
    return _safe_div(base, _rolling_std(base, 252))

def raut_171_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 109 return autocorrelation over 5d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=5), raw=True)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def raut_172_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 109 return autocorrelation over 21d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=5), raw=True)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def raut_173_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 109 return autocorrelation over 63d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=5), raw=True)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def raut_174_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 109 return autocorrelation over 126d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=5), raw=True)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def raut_175_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 109 return autocorrelation over 252d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=5), raw=True)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def raut_176_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 109 return autocorrelation over a 5d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=6), raw=True)
    return _rolling_mean(base, 5)

def raut_177_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 109 return autocorrelation over a 21d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=6), raw=True)
    return _rolling_mean(base, 21)

def raut_178_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 109 return autocorrelation over a 63d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=6), raw=True)
    return _rolling_mean(base, 63)

def raut_179_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 109 return autocorrelation over a 126d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=6), raw=True)
    return _rolling_mean(base, 126)

def raut_180_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 109 return autocorrelation over a 252d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=6), raw=True)
    return _rolling_mean(base, 252)

def raut_181_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 109 return autocorrelation by measuring deviations from the 5d mean.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=6), raw=True)
    return _zscore_rolling(base, 5)

def raut_182_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 109 return autocorrelation by measuring deviations from the 21d mean.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=6), raw=True)
    return _zscore_rolling(base, 21)

def raut_183_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 109 return autocorrelation by measuring deviations from the 63d mean.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=6), raw=True)
    return _zscore_rolling(base, 63)

def raut_184_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 109 return autocorrelation by measuring deviations from the 126d mean.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=6), raw=True)
    return _zscore_rolling(base, 126)

def raut_185_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 109 return autocorrelation by measuring deviations from the 252d mean.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=6), raw=True)
    return _zscore_rolling(base, 252)

def raut_186_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 109 return autocorrelation to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=6), raw=True)
    return _rank_pct(base, 5)

def raut_187_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 109 return autocorrelation to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=6), raw=True)
    return _rank_pct(base, 21)

def raut_188_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 109 return autocorrelation to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=6), raw=True)
    return _rank_pct(base, 63)

def raut_189_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 109 return autocorrelation to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=6), raw=True)
    return _rank_pct(base, 126)

def raut_190_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 109 return autocorrelation to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=6), raw=True)
    return _rank_pct(base, 252)

def raut_191_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 109 return autocorrelation distribution over 5d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=6), raw=True)
    return _rolling_skew(base, 5)

def raut_192_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 109 return autocorrelation distribution over 21d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=6), raw=True)
    return _rolling_skew(base, 21)

def raut_193_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 109 return autocorrelation distribution over 63d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=6), raw=True)
    return _rolling_skew(base, 63)

def raut_194_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 109 return autocorrelation distribution over 126d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=6), raw=True)
    return _rolling_skew(base, 126)

def raut_195_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 109 return autocorrelation distribution over 252d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=6), raw=True)
    return _rolling_skew(base, 252)

def raut_196_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 109 return autocorrelation over 5d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=6), raw=True)
    return _rolling_kurt(base, 5)

def raut_197_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 109 return autocorrelation over 21d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=6), raw=True)
    return _rolling_kurt(base, 21)

def raut_198_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 109 return autocorrelation over 63d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=6), raw=True)
    return _rolling_kurt(base, 63)

def raut_199_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 109 return autocorrelation over 126d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=6), raw=True)
    return _rolling_kurt(base, 126)

def raut_200_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 109 return autocorrelation over 252d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=6), raw=True)
    return _rolling_kurt(base, 252)

def raut_201_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 109 return autocorrelation for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=6), raw=True)
    return _safe_div(base, _rolling_std(base, 5))

def raut_202_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 109 return autocorrelation for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=6), raw=True)
    return _safe_div(base, _rolling_std(base, 21))

def raut_203_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 109 return autocorrelation for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=6), raw=True)
    return _safe_div(base, _rolling_std(base, 63))

def raut_204_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 109 return autocorrelation for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=6), raw=True)
    return _safe_div(base, _rolling_std(base, 126))

def raut_205_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 109 return autocorrelation for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=6), raw=True)
    return _safe_div(base, _rolling_std(base, 252))

def raut_206_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 109 return autocorrelation over 5d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=6), raw=True)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def raut_207_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 109 return autocorrelation over 21d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=6), raw=True)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def raut_208_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 109 return autocorrelation over 63d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=6), raw=True)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def raut_209_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 109 return autocorrelation over 126d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=6), raw=True)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def raut_210_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 109 return autocorrelation over 252d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=6), raw=True)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def raut_211_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 109 return autocorrelation over a 5d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=7), raw=True)
    return _rolling_mean(base, 5)

def raut_212_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 109 return autocorrelation over a 21d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=7), raw=True)
    return _rolling_mean(base, 21)

def raut_213_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 109 return autocorrelation over a 63d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=7), raw=True)
    return _rolling_mean(base, 63)

def raut_214_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 109 return autocorrelation over a 126d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=7), raw=True)
    return _rolling_mean(base, 126)

def raut_215_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 109 return autocorrelation over a 252d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=7), raw=True)
    return _rolling_mean(base, 252)

def raut_216_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 109 return autocorrelation by measuring deviations from the 5d mean.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=7), raw=True)
    return _zscore_rolling(base, 5)

def raut_217_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 109 return autocorrelation by measuring deviations from the 21d mean.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=7), raw=True)
    return _zscore_rolling(base, 21)

def raut_218_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 109 return autocorrelation by measuring deviations from the 63d mean.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=7), raw=True)
    return _zscore_rolling(base, 63)

def raut_219_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 109 return autocorrelation by measuring deviations from the 126d mean.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=7), raw=True)
    return _zscore_rolling(base, 126)

def raut_220_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 109 return autocorrelation by measuring deviations from the 252d mean.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=7), raw=True)
    return _zscore_rolling(base, 252)

def raut_221_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 109 return autocorrelation to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=7), raw=True)
    return _rank_pct(base, 5)

def raut_222_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 109 return autocorrelation to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=7), raw=True)
    return _rank_pct(base, 21)

def raut_223_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 109 return autocorrelation to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=7), raw=True)
    return _rank_pct(base, 63)

def raut_224_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 109 return autocorrelation to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=7), raw=True)
    return _rank_pct(base, 126)

def raut_225_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 109 return autocorrelation to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=7), raw=True)
    return _rank_pct(base, 252)
