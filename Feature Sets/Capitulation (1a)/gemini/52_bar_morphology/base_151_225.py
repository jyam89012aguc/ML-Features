"""
52_52_bar_morphology — Base Features 151-225
Domain: 52_bar_morphology
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

def bmor_151_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 52 bar morphology to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = (high - low) / close.rolling(21).std().replace(0, 1e-9)
    return _rank_pct(base, 5)

def bmor_152_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 52 bar morphology to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = (high - low) / close.rolling(21).std().replace(0, 1e-9)
    return _rank_pct(base, 21)

def bmor_153_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 52 bar morphology to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = (high - low) / close.rolling(21).std().replace(0, 1e-9)
    return _rank_pct(base, 63)

def bmor_154_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 52 bar morphology to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = (high - low) / close.rolling(21).std().replace(0, 1e-9)
    return _rank_pct(base, 126)

def bmor_155_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 52 bar morphology to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = (high - low) / close.rolling(21).std().replace(0, 1e-9)
    return _rank_pct(base, 252)

def bmor_156_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 52 bar morphology distribution over 5d to detect tail risk or exhaustion.
    """
    base = (high - low) / close.rolling(21).std().replace(0, 1e-9)
    return _rolling_skew(base, 5)

def bmor_157_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 52 bar morphology distribution over 21d to detect tail risk or exhaustion.
    """
    base = (high - low) / close.rolling(21).std().replace(0, 1e-9)
    return _rolling_skew(base, 21)

def bmor_158_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 52 bar morphology distribution over 63d to detect tail risk or exhaustion.
    """
    base = (high - low) / close.rolling(21).std().replace(0, 1e-9)
    return _rolling_skew(base, 63)

def bmor_159_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 52 bar morphology distribution over 126d to detect tail risk or exhaustion.
    """
    base = (high - low) / close.rolling(21).std().replace(0, 1e-9)
    return _rolling_skew(base, 126)

def bmor_160_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 52 bar morphology distribution over 252d to detect tail risk or exhaustion.
    """
    base = (high - low) / close.rolling(21).std().replace(0, 1e-9)
    return _rolling_skew(base, 252)

def bmor_161_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 52 bar morphology over 5d to capture explosive breakdown or reversal points.
    """
    base = (high - low) / close.rolling(21).std().replace(0, 1e-9)
    return _rolling_kurt(base, 5)

def bmor_162_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 52 bar morphology over 21d to capture explosive breakdown or reversal points.
    """
    base = (high - low) / close.rolling(21).std().replace(0, 1e-9)
    return _rolling_kurt(base, 21)

def bmor_163_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 52 bar morphology over 63d to capture explosive breakdown or reversal points.
    """
    base = (high - low) / close.rolling(21).std().replace(0, 1e-9)
    return _rolling_kurt(base, 63)

def bmor_164_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 52 bar morphology over 126d to capture explosive breakdown or reversal points.
    """
    base = (high - low) / close.rolling(21).std().replace(0, 1e-9)
    return _rolling_kurt(base, 126)

def bmor_165_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 52 bar morphology over 252d to capture explosive breakdown or reversal points.
    """
    base = (high - low) / close.rolling(21).std().replace(0, 1e-9)
    return _rolling_kurt(base, 252)

def bmor_166_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 52 bar morphology for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = (high - low) / close.rolling(21).std().replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 5))

def bmor_167_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 52 bar morphology for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = (high - low) / close.rolling(21).std().replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 21))

def bmor_168_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 52 bar morphology for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = (high - low) / close.rolling(21).std().replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 63))

def bmor_169_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 52 bar morphology for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = (high - low) / close.rolling(21).std().replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 126))

def bmor_170_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 52 bar morphology for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = (high - low) / close.rolling(21).std().replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 252))

def bmor_171_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 52 bar morphology over 5d to stabilize variance and capture exponential shifts.
    """
    base = (high - low) / close.rolling(21).std().replace(0, 1e-9)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def bmor_172_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 52 bar morphology over 21d to stabilize variance and capture exponential shifts.
    """
    base = (high - low) / close.rolling(21).std().replace(0, 1e-9)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def bmor_173_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 52 bar morphology over 63d to stabilize variance and capture exponential shifts.
    """
    base = (high - low) / close.rolling(21).std().replace(0, 1e-9)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def bmor_174_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 52 bar morphology over 126d to stabilize variance and capture exponential shifts.
    """
    base = (high - low) / close.rolling(21).std().replace(0, 1e-9)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def bmor_175_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 52 bar morphology over 252d to stabilize variance and capture exponential shifts.
    """
    base = (high - low) / close.rolling(21).std().replace(0, 1e-9)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def bmor_176_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 52 bar morphology over a 5d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(30).mean())
    return _rolling_mean(base, 5)

def bmor_177_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 52 bar morphology over a 21d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(30).mean())
    return _rolling_mean(base, 21)

def bmor_178_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 52 bar morphology over a 63d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(30).mean())
    return _rolling_mean(base, 63)

def bmor_179_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 52 bar morphology over a 126d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(30).mean())
    return _rolling_mean(base, 126)

def bmor_180_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 52 bar morphology over a 252d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(30).mean())
    return _rolling_mean(base, 252)

def bmor_181_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 52 bar morphology by measuring deviations from the 5d mean.
    """
    base = ((close - open).abs().rolling(30).mean())
    return _zscore_rolling(base, 5)

def bmor_182_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 52 bar morphology by measuring deviations from the 21d mean.
    """
    base = ((close - open).abs().rolling(30).mean())
    return _zscore_rolling(base, 21)

def bmor_183_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 52 bar morphology by measuring deviations from the 63d mean.
    """
    base = ((close - open).abs().rolling(30).mean())
    return _zscore_rolling(base, 63)

def bmor_184_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 52 bar morphology by measuring deviations from the 126d mean.
    """
    base = ((close - open).abs().rolling(30).mean())
    return _zscore_rolling(base, 126)

def bmor_185_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 52 bar morphology by measuring deviations from the 252d mean.
    """
    base = ((close - open).abs().rolling(30).mean())
    return _zscore_rolling(base, 252)

def bmor_186_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 52 bar morphology to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(30).mean())
    return _rank_pct(base, 5)

def bmor_187_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 52 bar morphology to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(30).mean())
    return _rank_pct(base, 21)

def bmor_188_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 52 bar morphology to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(30).mean())
    return _rank_pct(base, 63)

def bmor_189_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 52 bar morphology to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(30).mean())
    return _rank_pct(base, 126)

def bmor_190_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 52 bar morphology to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(30).mean())
    return _rank_pct(base, 252)

def bmor_191_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 52 bar morphology distribution over 5d to detect tail risk or exhaustion.
    """
    base = ((close - open).abs().rolling(30).mean())
    return _rolling_skew(base, 5)

def bmor_192_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 52 bar morphology distribution over 21d to detect tail risk or exhaustion.
    """
    base = ((close - open).abs().rolling(30).mean())
    return _rolling_skew(base, 21)

def bmor_193_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 52 bar morphology distribution over 63d to detect tail risk or exhaustion.
    """
    base = ((close - open).abs().rolling(30).mean())
    return _rolling_skew(base, 63)

def bmor_194_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 52 bar morphology distribution over 126d to detect tail risk or exhaustion.
    """
    base = ((close - open).abs().rolling(30).mean())
    return _rolling_skew(base, 126)

def bmor_195_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 52 bar morphology distribution over 252d to detect tail risk or exhaustion.
    """
    base = ((close - open).abs().rolling(30).mean())
    return _rolling_skew(base, 252)

def bmor_196_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 52 bar morphology over 5d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(30).mean())
    return _rolling_kurt(base, 5)

def bmor_197_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 52 bar morphology over 21d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(30).mean())
    return _rolling_kurt(base, 21)

def bmor_198_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 52 bar morphology over 63d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(30).mean())
    return _rolling_kurt(base, 63)

def bmor_199_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 52 bar morphology over 126d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(30).mean())
    return _rolling_kurt(base, 126)

def bmor_200_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 52 bar morphology over 252d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(30).mean())
    return _rolling_kurt(base, 252)

def bmor_201_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 52 bar morphology for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = ((close - open).abs().rolling(30).mean())
    return _safe_div(base, _rolling_std(base, 5))

def bmor_202_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 52 bar morphology for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = ((close - open).abs().rolling(30).mean())
    return _safe_div(base, _rolling_std(base, 21))

def bmor_203_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 52 bar morphology for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = ((close - open).abs().rolling(30).mean())
    return _safe_div(base, _rolling_std(base, 63))

def bmor_204_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 52 bar morphology for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = ((close - open).abs().rolling(30).mean())
    return _safe_div(base, _rolling_std(base, 126))

def bmor_205_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 52 bar morphology for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = ((close - open).abs().rolling(30).mean())
    return _safe_div(base, _rolling_std(base, 252))

def bmor_206_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 52 bar morphology over 5d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(30).mean())
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def bmor_207_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 52 bar morphology over 21d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(30).mean())
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def bmor_208_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 52 bar morphology over 63d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(30).mean())
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def bmor_209_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 52 bar morphology over 126d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(30).mean())
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def bmor_210_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 52 bar morphology over 252d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(30).mean())
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def bmor_211_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 52 bar morphology over a 5d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(35).mean())
    return _rolling_mean(base, 5)

def bmor_212_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 52 bar morphology over a 21d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(35).mean())
    return _rolling_mean(base, 21)

def bmor_213_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 52 bar morphology over a 63d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(35).mean())
    return _rolling_mean(base, 63)

def bmor_214_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 52 bar morphology over a 126d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(35).mean())
    return _rolling_mean(base, 126)

def bmor_215_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 52 bar morphology over a 252d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(35).mean())
    return _rolling_mean(base, 252)

def bmor_216_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 52 bar morphology by measuring deviations from the 5d mean.
    """
    base = ((close - open).abs().rolling(35).mean())
    return _zscore_rolling(base, 5)

def bmor_217_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 52 bar morphology by measuring deviations from the 21d mean.
    """
    base = ((close - open).abs().rolling(35).mean())
    return _zscore_rolling(base, 21)

def bmor_218_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 52 bar morphology by measuring deviations from the 63d mean.
    """
    base = ((close - open).abs().rolling(35).mean())
    return _zscore_rolling(base, 63)

def bmor_219_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 52 bar morphology by measuring deviations from the 126d mean.
    """
    base = ((close - open).abs().rolling(35).mean())
    return _zscore_rolling(base, 126)

def bmor_220_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 52 bar morphology by measuring deviations from the 252d mean.
    """
    base = ((close - open).abs().rolling(35).mean())
    return _zscore_rolling(base, 252)

def bmor_221_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 52 bar morphology to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(35).mean())
    return _rank_pct(base, 5)

def bmor_222_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 52 bar morphology to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(35).mean())
    return _rank_pct(base, 21)

def bmor_223_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 52 bar morphology to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(35).mean())
    return _rank_pct(base, 63)

def bmor_224_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 52 bar morphology to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(35).mean())
    return _rank_pct(base, 126)

def bmor_225_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 52 bar morphology to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(35).mean())
    return _rank_pct(base, 252)
