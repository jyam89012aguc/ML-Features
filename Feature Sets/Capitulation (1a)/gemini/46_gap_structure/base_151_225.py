"""
46_46_gap_structure — Base Features 151-225
Domain: 46_gap_structure
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

def gaps_151_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 46 gap structure to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = (high - low) / close.rolling(21).std().replace(0, 1e-9)
    return _rank_pct(base, 5)

def gaps_152_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 46 gap structure to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = (high - low) / close.rolling(21).std().replace(0, 1e-9)
    return _rank_pct(base, 21)

def gaps_153_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 46 gap structure to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = (high - low) / close.rolling(21).std().replace(0, 1e-9)
    return _rank_pct(base, 63)

def gaps_154_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 46 gap structure to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = (high - low) / close.rolling(21).std().replace(0, 1e-9)
    return _rank_pct(base, 126)

def gaps_155_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 46 gap structure to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = (high - low) / close.rolling(21).std().replace(0, 1e-9)
    return _rank_pct(base, 252)

def gaps_156_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 46 gap structure distribution over 5d to detect tail risk or exhaustion.
    """
    base = (high - low) / close.rolling(21).std().replace(0, 1e-9)
    return _rolling_skew(base, 5)

def gaps_157_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 46 gap structure distribution over 21d to detect tail risk or exhaustion.
    """
    base = (high - low) / close.rolling(21).std().replace(0, 1e-9)
    return _rolling_skew(base, 21)

def gaps_158_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 46 gap structure distribution over 63d to detect tail risk or exhaustion.
    """
    base = (high - low) / close.rolling(21).std().replace(0, 1e-9)
    return _rolling_skew(base, 63)

def gaps_159_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 46 gap structure distribution over 126d to detect tail risk or exhaustion.
    """
    base = (high - low) / close.rolling(21).std().replace(0, 1e-9)
    return _rolling_skew(base, 126)

def gaps_160_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 46 gap structure distribution over 252d to detect tail risk or exhaustion.
    """
    base = (high - low) / close.rolling(21).std().replace(0, 1e-9)
    return _rolling_skew(base, 252)

def gaps_161_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 46 gap structure over 5d to capture explosive breakdown or reversal points.
    """
    base = (high - low) / close.rolling(21).std().replace(0, 1e-9)
    return _rolling_kurt(base, 5)

def gaps_162_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 46 gap structure over 21d to capture explosive breakdown or reversal points.
    """
    base = (high - low) / close.rolling(21).std().replace(0, 1e-9)
    return _rolling_kurt(base, 21)

def gaps_163_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 46 gap structure over 63d to capture explosive breakdown or reversal points.
    """
    base = (high - low) / close.rolling(21).std().replace(0, 1e-9)
    return _rolling_kurt(base, 63)

def gaps_164_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 46 gap structure over 126d to capture explosive breakdown or reversal points.
    """
    base = (high - low) / close.rolling(21).std().replace(0, 1e-9)
    return _rolling_kurt(base, 126)

def gaps_165_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 46 gap structure over 252d to capture explosive breakdown or reversal points.
    """
    base = (high - low) / close.rolling(21).std().replace(0, 1e-9)
    return _rolling_kurt(base, 252)

def gaps_166_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 46 gap structure for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = (high - low) / close.rolling(21).std().replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 5))

def gaps_167_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 46 gap structure for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = (high - low) / close.rolling(21).std().replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 21))

def gaps_168_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 46 gap structure for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = (high - low) / close.rolling(21).std().replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 63))

def gaps_169_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 46 gap structure for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = (high - low) / close.rolling(21).std().replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 126))

def gaps_170_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 46 gap structure for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = (high - low) / close.rolling(21).std().replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 252))

def gaps_171_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 46 gap structure over 5d to stabilize variance and capture exponential shifts.
    """
    base = (high - low) / close.rolling(21).std().replace(0, 1e-9)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def gaps_172_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 46 gap structure over 21d to stabilize variance and capture exponential shifts.
    """
    base = (high - low) / close.rolling(21).std().replace(0, 1e-9)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def gaps_173_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 46 gap structure over 63d to stabilize variance and capture exponential shifts.
    """
    base = (high - low) / close.rolling(21).std().replace(0, 1e-9)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def gaps_174_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 46 gap structure over 126d to stabilize variance and capture exponential shifts.
    """
    base = (high - low) / close.rolling(21).std().replace(0, 1e-9)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def gaps_175_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 46 gap structure over 252d to stabilize variance and capture exponential shifts.
    """
    base = (high - low) / close.rolling(21).std().replace(0, 1e-9)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def gaps_176_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 46 gap structure over a 5d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(30).mean())
    return _rolling_mean(base, 5)

def gaps_177_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 46 gap structure over a 21d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(30).mean())
    return _rolling_mean(base, 21)

def gaps_178_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 46 gap structure over a 63d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(30).mean())
    return _rolling_mean(base, 63)

def gaps_179_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 46 gap structure over a 126d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(30).mean())
    return _rolling_mean(base, 126)

def gaps_180_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 46 gap structure over a 252d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(30).mean())
    return _rolling_mean(base, 252)

def gaps_181_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 46 gap structure by measuring deviations from the 5d mean.
    """
    base = ((close - open).abs().rolling(30).mean())
    return _zscore_rolling(base, 5)

def gaps_182_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 46 gap structure by measuring deviations from the 21d mean.
    """
    base = ((close - open).abs().rolling(30).mean())
    return _zscore_rolling(base, 21)

def gaps_183_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 46 gap structure by measuring deviations from the 63d mean.
    """
    base = ((close - open).abs().rolling(30).mean())
    return _zscore_rolling(base, 63)

def gaps_184_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 46 gap structure by measuring deviations from the 126d mean.
    """
    base = ((close - open).abs().rolling(30).mean())
    return _zscore_rolling(base, 126)

def gaps_185_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 46 gap structure by measuring deviations from the 252d mean.
    """
    base = ((close - open).abs().rolling(30).mean())
    return _zscore_rolling(base, 252)

def gaps_186_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 46 gap structure to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(30).mean())
    return _rank_pct(base, 5)

def gaps_187_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 46 gap structure to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(30).mean())
    return _rank_pct(base, 21)

def gaps_188_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 46 gap structure to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(30).mean())
    return _rank_pct(base, 63)

def gaps_189_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 46 gap structure to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(30).mean())
    return _rank_pct(base, 126)

def gaps_190_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 46 gap structure to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(30).mean())
    return _rank_pct(base, 252)

def gaps_191_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 46 gap structure distribution over 5d to detect tail risk or exhaustion.
    """
    base = ((close - open).abs().rolling(30).mean())
    return _rolling_skew(base, 5)

def gaps_192_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 46 gap structure distribution over 21d to detect tail risk or exhaustion.
    """
    base = ((close - open).abs().rolling(30).mean())
    return _rolling_skew(base, 21)

def gaps_193_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 46 gap structure distribution over 63d to detect tail risk or exhaustion.
    """
    base = ((close - open).abs().rolling(30).mean())
    return _rolling_skew(base, 63)

def gaps_194_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 46 gap structure distribution over 126d to detect tail risk or exhaustion.
    """
    base = ((close - open).abs().rolling(30).mean())
    return _rolling_skew(base, 126)

def gaps_195_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 46 gap structure distribution over 252d to detect tail risk or exhaustion.
    """
    base = ((close - open).abs().rolling(30).mean())
    return _rolling_skew(base, 252)

def gaps_196_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 46 gap structure over 5d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(30).mean())
    return _rolling_kurt(base, 5)

def gaps_197_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 46 gap structure over 21d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(30).mean())
    return _rolling_kurt(base, 21)

def gaps_198_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 46 gap structure over 63d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(30).mean())
    return _rolling_kurt(base, 63)

def gaps_199_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 46 gap structure over 126d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(30).mean())
    return _rolling_kurt(base, 126)

def gaps_200_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 46 gap structure over 252d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(30).mean())
    return _rolling_kurt(base, 252)

def gaps_201_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 46 gap structure for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = ((close - open).abs().rolling(30).mean())
    return _safe_div(base, _rolling_std(base, 5))

def gaps_202_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 46 gap structure for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = ((close - open).abs().rolling(30).mean())
    return _safe_div(base, _rolling_std(base, 21))

def gaps_203_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 46 gap structure for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = ((close - open).abs().rolling(30).mean())
    return _safe_div(base, _rolling_std(base, 63))

def gaps_204_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 46 gap structure for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = ((close - open).abs().rolling(30).mean())
    return _safe_div(base, _rolling_std(base, 126))

def gaps_205_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 46 gap structure for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = ((close - open).abs().rolling(30).mean())
    return _safe_div(base, _rolling_std(base, 252))

def gaps_206_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 46 gap structure over 5d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(30).mean())
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def gaps_207_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 46 gap structure over 21d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(30).mean())
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def gaps_208_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 46 gap structure over 63d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(30).mean())
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def gaps_209_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 46 gap structure over 126d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(30).mean())
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def gaps_210_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 46 gap structure over 252d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(30).mean())
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def gaps_211_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 46 gap structure over a 5d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(35).mean())
    return _rolling_mean(base, 5)

def gaps_212_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 46 gap structure over a 21d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(35).mean())
    return _rolling_mean(base, 21)

def gaps_213_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 46 gap structure over a 63d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(35).mean())
    return _rolling_mean(base, 63)

def gaps_214_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 46 gap structure over a 126d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(35).mean())
    return _rolling_mean(base, 126)

def gaps_215_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 46 gap structure over a 252d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(35).mean())
    return _rolling_mean(base, 252)

def gaps_216_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 46 gap structure by measuring deviations from the 5d mean.
    """
    base = ((close - open).abs().rolling(35).mean())
    return _zscore_rolling(base, 5)

def gaps_217_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 46 gap structure by measuring deviations from the 21d mean.
    """
    base = ((close - open).abs().rolling(35).mean())
    return _zscore_rolling(base, 21)

def gaps_218_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 46 gap structure by measuring deviations from the 63d mean.
    """
    base = ((close - open).abs().rolling(35).mean())
    return _zscore_rolling(base, 63)

def gaps_219_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 46 gap structure by measuring deviations from the 126d mean.
    """
    base = ((close - open).abs().rolling(35).mean())
    return _zscore_rolling(base, 126)

def gaps_220_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 46 gap structure by measuring deviations from the 252d mean.
    """
    base = ((close - open).abs().rolling(35).mean())
    return _zscore_rolling(base, 252)

def gaps_221_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 46 gap structure to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(35).mean())
    return _rank_pct(base, 5)

def gaps_222_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 46 gap structure to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(35).mean())
    return _rank_pct(base, 21)

def gaps_223_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 46 gap structure to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(35).mean())
    return _rank_pct(base, 63)

def gaps_224_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 46 gap structure to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(35).mean())
    return _rank_pct(base, 126)

def gaps_225_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 46 gap structure to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(35).mean())
    return _rank_pct(base, 252)
