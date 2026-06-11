"""
24_24_volume_distribution — Base Features 151-225
Domain: 24_volume_distribution
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

def vdis_151_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 24 volume distribution to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = (volume.pct_change(5).rolling(25).mean())
    return _rank_pct(base, 5)

def vdis_152_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 24 volume distribution to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = (volume.pct_change(5).rolling(25).mean())
    return _rank_pct(base, 21)

def vdis_153_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 24 volume distribution to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = (volume.pct_change(5).rolling(25).mean())
    return _rank_pct(base, 63)

def vdis_154_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 24 volume distribution to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = (volume.pct_change(5).rolling(25).mean())
    return _rank_pct(base, 126)

def vdis_155_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 24 volume distribution to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = (volume.pct_change(5).rolling(25).mean())
    return _rank_pct(base, 252)

def vdis_156_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 24 volume distribution distribution over 5d to detect tail risk or exhaustion.
    """
    base = (volume.pct_change(5).rolling(25).mean())
    return _rolling_skew(base, 5)

def vdis_157_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 24 volume distribution distribution over 21d to detect tail risk or exhaustion.
    """
    base = (volume.pct_change(5).rolling(25).mean())
    return _rolling_skew(base, 21)

def vdis_158_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 24 volume distribution distribution over 63d to detect tail risk or exhaustion.
    """
    base = (volume.pct_change(5).rolling(25).mean())
    return _rolling_skew(base, 63)

def vdis_159_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 24 volume distribution distribution over 126d to detect tail risk or exhaustion.
    """
    base = (volume.pct_change(5).rolling(25).mean())
    return _rolling_skew(base, 126)

def vdis_160_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 24 volume distribution distribution over 252d to detect tail risk or exhaustion.
    """
    base = (volume.pct_change(5).rolling(25).mean())
    return _rolling_skew(base, 252)

def vdis_161_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 24 volume distribution over 5d to capture explosive breakdown or reversal points.
    """
    base = (volume.pct_change(5).rolling(25).mean())
    return _rolling_kurt(base, 5)

def vdis_162_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 24 volume distribution over 21d to capture explosive breakdown or reversal points.
    """
    base = (volume.pct_change(5).rolling(25).mean())
    return _rolling_kurt(base, 21)

def vdis_163_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 24 volume distribution over 63d to capture explosive breakdown or reversal points.
    """
    base = (volume.pct_change(5).rolling(25).mean())
    return _rolling_kurt(base, 63)

def vdis_164_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 24 volume distribution over 126d to capture explosive breakdown or reversal points.
    """
    base = (volume.pct_change(5).rolling(25).mean())
    return _rolling_kurt(base, 126)

def vdis_165_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 24 volume distribution over 252d to capture explosive breakdown or reversal points.
    """
    base = (volume.pct_change(5).rolling(25).mean())
    return _rolling_kurt(base, 252)

def vdis_166_voladj_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 24 volume distribution for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = (volume.pct_change(5).rolling(25).mean())
    return _safe_div(base, _rolling_std(base, 5))

def vdis_167_voladj_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 24 volume distribution for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = (volume.pct_change(5).rolling(25).mean())
    return _safe_div(base, _rolling_std(base, 21))

def vdis_168_voladj_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 24 volume distribution for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = (volume.pct_change(5).rolling(25).mean())
    return _safe_div(base, _rolling_std(base, 63))

def vdis_169_voladj_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 24 volume distribution for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = (volume.pct_change(5).rolling(25).mean())
    return _safe_div(base, _rolling_std(base, 126))

def vdis_170_voladj_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 24 volume distribution for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = (volume.pct_change(5).rolling(25).mean())
    return _safe_div(base, _rolling_std(base, 252))

def vdis_171_lognorm_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 24 volume distribution over 5d to stabilize variance and capture exponential shifts.
    """
    base = (volume.pct_change(5).rolling(25).mean())
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def vdis_172_lognorm_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 24 volume distribution over 21d to stabilize variance and capture exponential shifts.
    """
    base = (volume.pct_change(5).rolling(25).mean())
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def vdis_173_lognorm_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 24 volume distribution over 63d to stabilize variance and capture exponential shifts.
    """
    base = (volume.pct_change(5).rolling(25).mean())
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def vdis_174_lognorm_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 24 volume distribution over 126d to stabilize variance and capture exponential shifts.
    """
    base = (volume.pct_change(5).rolling(25).mean())
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def vdis_175_lognorm_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 24 volume distribution over 252d to stabilize variance and capture exponential shifts.
    """
    base = (volume.pct_change(5).rolling(25).mean())
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def vdis_176_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 24 volume distribution over a 5d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(6).rolling(30).mean())
    return _rolling_mean(base, 5)

def vdis_177_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 24 volume distribution over a 21d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(6).rolling(30).mean())
    return _rolling_mean(base, 21)

def vdis_178_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 24 volume distribution over a 63d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(6).rolling(30).mean())
    return _rolling_mean(base, 63)

def vdis_179_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 24 volume distribution over a 126d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(6).rolling(30).mean())
    return _rolling_mean(base, 126)

def vdis_180_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 24 volume distribution over a 252d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(6).rolling(30).mean())
    return _rolling_mean(base, 252)

def vdis_181_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 24 volume distribution by measuring deviations from the 5d mean.
    """
    base = (volume.pct_change(6).rolling(30).mean())
    return _zscore_rolling(base, 5)

def vdis_182_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 24 volume distribution by measuring deviations from the 21d mean.
    """
    base = (volume.pct_change(6).rolling(30).mean())
    return _zscore_rolling(base, 21)

def vdis_183_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 24 volume distribution by measuring deviations from the 63d mean.
    """
    base = (volume.pct_change(6).rolling(30).mean())
    return _zscore_rolling(base, 63)

def vdis_184_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 24 volume distribution by measuring deviations from the 126d mean.
    """
    base = (volume.pct_change(6).rolling(30).mean())
    return _zscore_rolling(base, 126)

def vdis_185_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 24 volume distribution by measuring deviations from the 252d mean.
    """
    base = (volume.pct_change(6).rolling(30).mean())
    return _zscore_rolling(base, 252)

def vdis_186_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 24 volume distribution to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = (volume.pct_change(6).rolling(30).mean())
    return _rank_pct(base, 5)

def vdis_187_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 24 volume distribution to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = (volume.pct_change(6).rolling(30).mean())
    return _rank_pct(base, 21)

def vdis_188_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 24 volume distribution to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = (volume.pct_change(6).rolling(30).mean())
    return _rank_pct(base, 63)

def vdis_189_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 24 volume distribution to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = (volume.pct_change(6).rolling(30).mean())
    return _rank_pct(base, 126)

def vdis_190_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 24 volume distribution to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = (volume.pct_change(6).rolling(30).mean())
    return _rank_pct(base, 252)

def vdis_191_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 24 volume distribution distribution over 5d to detect tail risk or exhaustion.
    """
    base = (volume.pct_change(6).rolling(30).mean())
    return _rolling_skew(base, 5)

def vdis_192_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 24 volume distribution distribution over 21d to detect tail risk or exhaustion.
    """
    base = (volume.pct_change(6).rolling(30).mean())
    return _rolling_skew(base, 21)

def vdis_193_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 24 volume distribution distribution over 63d to detect tail risk or exhaustion.
    """
    base = (volume.pct_change(6).rolling(30).mean())
    return _rolling_skew(base, 63)

def vdis_194_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 24 volume distribution distribution over 126d to detect tail risk or exhaustion.
    """
    base = (volume.pct_change(6).rolling(30).mean())
    return _rolling_skew(base, 126)

def vdis_195_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 24 volume distribution distribution over 252d to detect tail risk or exhaustion.
    """
    base = (volume.pct_change(6).rolling(30).mean())
    return _rolling_skew(base, 252)

def vdis_196_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 24 volume distribution over 5d to capture explosive breakdown or reversal points.
    """
    base = (volume.pct_change(6).rolling(30).mean())
    return _rolling_kurt(base, 5)

def vdis_197_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 24 volume distribution over 21d to capture explosive breakdown or reversal points.
    """
    base = (volume.pct_change(6).rolling(30).mean())
    return _rolling_kurt(base, 21)

def vdis_198_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 24 volume distribution over 63d to capture explosive breakdown or reversal points.
    """
    base = (volume.pct_change(6).rolling(30).mean())
    return _rolling_kurt(base, 63)

def vdis_199_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 24 volume distribution over 126d to capture explosive breakdown or reversal points.
    """
    base = (volume.pct_change(6).rolling(30).mean())
    return _rolling_kurt(base, 126)

def vdis_200_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 24 volume distribution over 252d to capture explosive breakdown or reversal points.
    """
    base = (volume.pct_change(6).rolling(30).mean())
    return _rolling_kurt(base, 252)

def vdis_201_voladj_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 24 volume distribution for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = (volume.pct_change(6).rolling(30).mean())
    return _safe_div(base, _rolling_std(base, 5))

def vdis_202_voladj_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 24 volume distribution for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = (volume.pct_change(6).rolling(30).mean())
    return _safe_div(base, _rolling_std(base, 21))

def vdis_203_voladj_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 24 volume distribution for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = (volume.pct_change(6).rolling(30).mean())
    return _safe_div(base, _rolling_std(base, 63))

def vdis_204_voladj_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 24 volume distribution for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = (volume.pct_change(6).rolling(30).mean())
    return _safe_div(base, _rolling_std(base, 126))

def vdis_205_voladj_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 24 volume distribution for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = (volume.pct_change(6).rolling(30).mean())
    return _safe_div(base, _rolling_std(base, 252))

def vdis_206_lognorm_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 24 volume distribution over 5d to stabilize variance and capture exponential shifts.
    """
    base = (volume.pct_change(6).rolling(30).mean())
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def vdis_207_lognorm_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 24 volume distribution over 21d to stabilize variance and capture exponential shifts.
    """
    base = (volume.pct_change(6).rolling(30).mean())
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def vdis_208_lognorm_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 24 volume distribution over 63d to stabilize variance and capture exponential shifts.
    """
    base = (volume.pct_change(6).rolling(30).mean())
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def vdis_209_lognorm_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 24 volume distribution over 126d to stabilize variance and capture exponential shifts.
    """
    base = (volume.pct_change(6).rolling(30).mean())
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def vdis_210_lognorm_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 24 volume distribution over 252d to stabilize variance and capture exponential shifts.
    """
    base = (volume.pct_change(6).rolling(30).mean())
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def vdis_211_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 24 volume distribution over a 5d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(7).rolling(35).mean())
    return _rolling_mean(base, 5)

def vdis_212_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 24 volume distribution over a 21d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(7).rolling(35).mean())
    return _rolling_mean(base, 21)

def vdis_213_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 24 volume distribution over a 63d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(7).rolling(35).mean())
    return _rolling_mean(base, 63)

def vdis_214_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 24 volume distribution over a 126d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(7).rolling(35).mean())
    return _rolling_mean(base, 126)

def vdis_215_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 24 volume distribution over a 252d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(7).rolling(35).mean())
    return _rolling_mean(base, 252)

def vdis_216_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 24 volume distribution by measuring deviations from the 5d mean.
    """
    base = (volume.pct_change(7).rolling(35).mean())
    return _zscore_rolling(base, 5)

def vdis_217_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 24 volume distribution by measuring deviations from the 21d mean.
    """
    base = (volume.pct_change(7).rolling(35).mean())
    return _zscore_rolling(base, 21)

def vdis_218_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 24 volume distribution by measuring deviations from the 63d mean.
    """
    base = (volume.pct_change(7).rolling(35).mean())
    return _zscore_rolling(base, 63)

def vdis_219_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 24 volume distribution by measuring deviations from the 126d mean.
    """
    base = (volume.pct_change(7).rolling(35).mean())
    return _zscore_rolling(base, 126)

def vdis_220_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 24 volume distribution by measuring deviations from the 252d mean.
    """
    base = (volume.pct_change(7).rolling(35).mean())
    return _zscore_rolling(base, 252)

def vdis_221_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 24 volume distribution to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = (volume.pct_change(7).rolling(35).mean())
    return _rank_pct(base, 5)

def vdis_222_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 24 volume distribution to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = (volume.pct_change(7).rolling(35).mean())
    return _rank_pct(base, 21)

def vdis_223_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 24 volume distribution to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = (volume.pct_change(7).rolling(35).mean())
    return _rank_pct(base, 63)

def vdis_224_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 24 volume distribution to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = (volume.pct_change(7).rolling(35).mean())
    return _rank_pct(base, 126)

def vdis_225_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 24 volume distribution to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = (volume.pct_change(7).rolling(35).mean())
    return _rank_pct(base, 252)
