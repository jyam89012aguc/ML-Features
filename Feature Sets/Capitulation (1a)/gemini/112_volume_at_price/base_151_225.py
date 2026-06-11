"""
112_112_volume_at_price — Base Features 151-225
Domain: 112_volume_at_price
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

def vapr_151_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 112 volume at price to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = volume * close.pct_change(5)
    return _rank_pct(base, 5)

def vapr_152_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 112 volume at price to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = volume * close.pct_change(5)
    return _rank_pct(base, 21)

def vapr_153_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 112 volume at price to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = volume * close.pct_change(5)
    return _rank_pct(base, 63)

def vapr_154_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 112 volume at price to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = volume * close.pct_change(5)
    return _rank_pct(base, 126)

def vapr_155_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 112 volume at price to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = volume * close.pct_change(5)
    return _rank_pct(base, 252)

def vapr_156_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 112 volume at price distribution over 5d to detect tail risk or exhaustion.
    """
    base = volume * close.pct_change(5)
    return _rolling_skew(base, 5)

def vapr_157_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 112 volume at price distribution over 21d to detect tail risk or exhaustion.
    """
    base = volume * close.pct_change(5)
    return _rolling_skew(base, 21)

def vapr_158_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 112 volume at price distribution over 63d to detect tail risk or exhaustion.
    """
    base = volume * close.pct_change(5)
    return _rolling_skew(base, 63)

def vapr_159_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 112 volume at price distribution over 126d to detect tail risk or exhaustion.
    """
    base = volume * close.pct_change(5)
    return _rolling_skew(base, 126)

def vapr_160_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 112 volume at price distribution over 252d to detect tail risk or exhaustion.
    """
    base = volume * close.pct_change(5)
    return _rolling_skew(base, 252)

def vapr_161_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 112 volume at price over 5d to capture explosive breakdown or reversal points.
    """
    base = volume * close.pct_change(5)
    return _rolling_kurt(base, 5)

def vapr_162_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 112 volume at price over 21d to capture explosive breakdown or reversal points.
    """
    base = volume * close.pct_change(5)
    return _rolling_kurt(base, 21)

def vapr_163_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 112 volume at price over 63d to capture explosive breakdown or reversal points.
    """
    base = volume * close.pct_change(5)
    return _rolling_kurt(base, 63)

def vapr_164_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 112 volume at price over 126d to capture explosive breakdown or reversal points.
    """
    base = volume * close.pct_change(5)
    return _rolling_kurt(base, 126)

def vapr_165_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 112 volume at price over 252d to capture explosive breakdown or reversal points.
    """
    base = volume * close.pct_change(5)
    return _rolling_kurt(base, 252)

def vapr_166_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 112 volume at price for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = volume * close.pct_change(5)
    return _safe_div(base, _rolling_std(base, 5))

def vapr_167_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 112 volume at price for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = volume * close.pct_change(5)
    return _safe_div(base, _rolling_std(base, 21))

def vapr_168_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 112 volume at price for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = volume * close.pct_change(5)
    return _safe_div(base, _rolling_std(base, 63))

def vapr_169_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 112 volume at price for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = volume * close.pct_change(5)
    return _safe_div(base, _rolling_std(base, 126))

def vapr_170_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 112 volume at price for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = volume * close.pct_change(5)
    return _safe_div(base, _rolling_std(base, 252))

def vapr_171_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 112 volume at price over 5d to stabilize variance and capture exponential shifts.
    """
    base = volume * close.pct_change(5)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def vapr_172_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 112 volume at price over 21d to stabilize variance and capture exponential shifts.
    """
    base = volume * close.pct_change(5)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def vapr_173_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 112 volume at price over 63d to stabilize variance and capture exponential shifts.
    """
    base = volume * close.pct_change(5)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def vapr_174_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 112 volume at price over 126d to stabilize variance and capture exponential shifts.
    """
    base = volume * close.pct_change(5)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def vapr_175_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 112 volume at price over 252d to stabilize variance and capture exponential shifts.
    """
    base = volume * close.pct_change(5)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def vapr_176_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 112 volume at price over a 5d horizon to identify extreme regimes.
    """
    base = volume * close.pct_change(6)
    return _rolling_mean(base, 5)

def vapr_177_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 112 volume at price over a 21d horizon to identify extreme regimes.
    """
    base = volume * close.pct_change(6)
    return _rolling_mean(base, 21)

def vapr_178_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 112 volume at price over a 63d horizon to identify extreme regimes.
    """
    base = volume * close.pct_change(6)
    return _rolling_mean(base, 63)

def vapr_179_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 112 volume at price over a 126d horizon to identify extreme regimes.
    """
    base = volume * close.pct_change(6)
    return _rolling_mean(base, 126)

def vapr_180_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 112 volume at price over a 252d horizon to identify extreme regimes.
    """
    base = volume * close.pct_change(6)
    return _rolling_mean(base, 252)

def vapr_181_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 112 volume at price by measuring deviations from the 5d mean.
    """
    base = volume * close.pct_change(6)
    return _zscore_rolling(base, 5)

def vapr_182_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 112 volume at price by measuring deviations from the 21d mean.
    """
    base = volume * close.pct_change(6)
    return _zscore_rolling(base, 21)

def vapr_183_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 112 volume at price by measuring deviations from the 63d mean.
    """
    base = volume * close.pct_change(6)
    return _zscore_rolling(base, 63)

def vapr_184_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 112 volume at price by measuring deviations from the 126d mean.
    """
    base = volume * close.pct_change(6)
    return _zscore_rolling(base, 126)

def vapr_185_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 112 volume at price by measuring deviations from the 252d mean.
    """
    base = volume * close.pct_change(6)
    return _zscore_rolling(base, 252)

def vapr_186_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 112 volume at price to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = volume * close.pct_change(6)
    return _rank_pct(base, 5)

def vapr_187_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 112 volume at price to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = volume * close.pct_change(6)
    return _rank_pct(base, 21)

def vapr_188_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 112 volume at price to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = volume * close.pct_change(6)
    return _rank_pct(base, 63)

def vapr_189_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 112 volume at price to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = volume * close.pct_change(6)
    return _rank_pct(base, 126)

def vapr_190_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 112 volume at price to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = volume * close.pct_change(6)
    return _rank_pct(base, 252)

def vapr_191_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 112 volume at price distribution over 5d to detect tail risk or exhaustion.
    """
    base = volume * close.pct_change(6)
    return _rolling_skew(base, 5)

def vapr_192_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 112 volume at price distribution over 21d to detect tail risk or exhaustion.
    """
    base = volume * close.pct_change(6)
    return _rolling_skew(base, 21)

def vapr_193_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 112 volume at price distribution over 63d to detect tail risk or exhaustion.
    """
    base = volume * close.pct_change(6)
    return _rolling_skew(base, 63)

def vapr_194_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 112 volume at price distribution over 126d to detect tail risk or exhaustion.
    """
    base = volume * close.pct_change(6)
    return _rolling_skew(base, 126)

def vapr_195_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 112 volume at price distribution over 252d to detect tail risk or exhaustion.
    """
    base = volume * close.pct_change(6)
    return _rolling_skew(base, 252)

def vapr_196_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 112 volume at price over 5d to capture explosive breakdown or reversal points.
    """
    base = volume * close.pct_change(6)
    return _rolling_kurt(base, 5)

def vapr_197_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 112 volume at price over 21d to capture explosive breakdown or reversal points.
    """
    base = volume * close.pct_change(6)
    return _rolling_kurt(base, 21)

def vapr_198_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 112 volume at price over 63d to capture explosive breakdown or reversal points.
    """
    base = volume * close.pct_change(6)
    return _rolling_kurt(base, 63)

def vapr_199_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 112 volume at price over 126d to capture explosive breakdown or reversal points.
    """
    base = volume * close.pct_change(6)
    return _rolling_kurt(base, 126)

def vapr_200_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 112 volume at price over 252d to capture explosive breakdown or reversal points.
    """
    base = volume * close.pct_change(6)
    return _rolling_kurt(base, 252)

def vapr_201_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 112 volume at price for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = volume * close.pct_change(6)
    return _safe_div(base, _rolling_std(base, 5))

def vapr_202_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 112 volume at price for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = volume * close.pct_change(6)
    return _safe_div(base, _rolling_std(base, 21))

def vapr_203_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 112 volume at price for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = volume * close.pct_change(6)
    return _safe_div(base, _rolling_std(base, 63))

def vapr_204_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 112 volume at price for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = volume * close.pct_change(6)
    return _safe_div(base, _rolling_std(base, 126))

def vapr_205_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 112 volume at price for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = volume * close.pct_change(6)
    return _safe_div(base, _rolling_std(base, 252))

def vapr_206_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 112 volume at price over 5d to stabilize variance and capture exponential shifts.
    """
    base = volume * close.pct_change(6)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def vapr_207_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 112 volume at price over 21d to stabilize variance and capture exponential shifts.
    """
    base = volume * close.pct_change(6)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def vapr_208_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 112 volume at price over 63d to stabilize variance and capture exponential shifts.
    """
    base = volume * close.pct_change(6)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def vapr_209_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 112 volume at price over 126d to stabilize variance and capture exponential shifts.
    """
    base = volume * close.pct_change(6)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def vapr_210_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 112 volume at price over 252d to stabilize variance and capture exponential shifts.
    """
    base = volume * close.pct_change(6)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def vapr_211_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 112 volume at price over a 5d horizon to identify extreme regimes.
    """
    base = volume * close.pct_change(7)
    return _rolling_mean(base, 5)

def vapr_212_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 112 volume at price over a 21d horizon to identify extreme regimes.
    """
    base = volume * close.pct_change(7)
    return _rolling_mean(base, 21)

def vapr_213_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 112 volume at price over a 63d horizon to identify extreme regimes.
    """
    base = volume * close.pct_change(7)
    return _rolling_mean(base, 63)

def vapr_214_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 112 volume at price over a 126d horizon to identify extreme regimes.
    """
    base = volume * close.pct_change(7)
    return _rolling_mean(base, 126)

def vapr_215_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 112 volume at price over a 252d horizon to identify extreme regimes.
    """
    base = volume * close.pct_change(7)
    return _rolling_mean(base, 252)

def vapr_216_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 112 volume at price by measuring deviations from the 5d mean.
    """
    base = volume * close.pct_change(7)
    return _zscore_rolling(base, 5)

def vapr_217_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 112 volume at price by measuring deviations from the 21d mean.
    """
    base = volume * close.pct_change(7)
    return _zscore_rolling(base, 21)

def vapr_218_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 112 volume at price by measuring deviations from the 63d mean.
    """
    base = volume * close.pct_change(7)
    return _zscore_rolling(base, 63)

def vapr_219_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 112 volume at price by measuring deviations from the 126d mean.
    """
    base = volume * close.pct_change(7)
    return _zscore_rolling(base, 126)

def vapr_220_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 112 volume at price by measuring deviations from the 252d mean.
    """
    base = volume * close.pct_change(7)
    return _zscore_rolling(base, 252)

def vapr_221_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 112 volume at price to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = volume * close.pct_change(7)
    return _rank_pct(base, 5)

def vapr_222_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 112 volume at price to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = volume * close.pct_change(7)
    return _rank_pct(base, 21)

def vapr_223_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 112 volume at price to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = volume * close.pct_change(7)
    return _rank_pct(base, 63)

def vapr_224_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 112 volume at price to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = volume * close.pct_change(7)
    return _rank_pct(base, 126)

def vapr_225_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 112 volume at price to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = volume * close.pct_change(7)
    return _rank_pct(base, 252)
