"""
59_59_market_impact_proxy — Base Features 151-225
Domain: 59_market_impact_proxy
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

def mimp_151_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 59 market impact proxy to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = close.pct_change().abs() / volume.replace(0, 1e-9)
    return _rank_pct(base, 5)

def mimp_152_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 59 market impact proxy to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = close.pct_change().abs() / volume.replace(0, 1e-9)
    return _rank_pct(base, 21)

def mimp_153_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 59 market impact proxy to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = close.pct_change().abs() / volume.replace(0, 1e-9)
    return _rank_pct(base, 63)

def mimp_154_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 59 market impact proxy to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = close.pct_change().abs() / volume.replace(0, 1e-9)
    return _rank_pct(base, 126)

def mimp_155_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 59 market impact proxy to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = close.pct_change().abs() / volume.replace(0, 1e-9)
    return _rank_pct(base, 252)

def mimp_156_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 59 market impact proxy distribution over 5d to detect tail risk or exhaustion.
    """
    base = close.pct_change().abs() / volume.replace(0, 1e-9)
    return _rolling_skew(base, 5)

def mimp_157_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 59 market impact proxy distribution over 21d to detect tail risk or exhaustion.
    """
    base = close.pct_change().abs() / volume.replace(0, 1e-9)
    return _rolling_skew(base, 21)

def mimp_158_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 59 market impact proxy distribution over 63d to detect tail risk or exhaustion.
    """
    base = close.pct_change().abs() / volume.replace(0, 1e-9)
    return _rolling_skew(base, 63)

def mimp_159_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 59 market impact proxy distribution over 126d to detect tail risk or exhaustion.
    """
    base = close.pct_change().abs() / volume.replace(0, 1e-9)
    return _rolling_skew(base, 126)

def mimp_160_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 59 market impact proxy distribution over 252d to detect tail risk or exhaustion.
    """
    base = close.pct_change().abs() / volume.replace(0, 1e-9)
    return _rolling_skew(base, 252)

def mimp_161_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 59 market impact proxy over 5d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().abs() / volume.replace(0, 1e-9)
    return _rolling_kurt(base, 5)

def mimp_162_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 59 market impact proxy over 21d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().abs() / volume.replace(0, 1e-9)
    return _rolling_kurt(base, 21)

def mimp_163_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 59 market impact proxy over 63d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().abs() / volume.replace(0, 1e-9)
    return _rolling_kurt(base, 63)

def mimp_164_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 59 market impact proxy over 126d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().abs() / volume.replace(0, 1e-9)
    return _rolling_kurt(base, 126)

def mimp_165_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 59 market impact proxy over 252d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().abs() / volume.replace(0, 1e-9)
    return _rolling_kurt(base, 252)

def mimp_166_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 59 market impact proxy for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().abs() / volume.replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 5))

def mimp_167_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 59 market impact proxy for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().abs() / volume.replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 21))

def mimp_168_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 59 market impact proxy for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().abs() / volume.replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 63))

def mimp_169_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 59 market impact proxy for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().abs() / volume.replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 126))

def mimp_170_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 59 market impact proxy for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().abs() / volume.replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 252))

def mimp_171_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 59 market impact proxy over 5d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().abs() / volume.replace(0, 1e-9)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def mimp_172_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 59 market impact proxy over 21d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().abs() / volume.replace(0, 1e-9)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def mimp_173_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 59 market impact proxy over 63d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().abs() / volume.replace(0, 1e-9)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def mimp_174_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 59 market impact proxy over 126d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().abs() / volume.replace(0, 1e-9)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def mimp_175_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 59 market impact proxy over 252d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().abs() / volume.replace(0, 1e-9)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def mimp_176_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 59 market impact proxy over a 5d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(6).rolling(30).mean())
    return _rolling_mean(base, 5)

def mimp_177_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 59 market impact proxy over a 21d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(6).rolling(30).mean())
    return _rolling_mean(base, 21)

def mimp_178_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 59 market impact proxy over a 63d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(6).rolling(30).mean())
    return _rolling_mean(base, 63)

def mimp_179_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 59 market impact proxy over a 126d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(6).rolling(30).mean())
    return _rolling_mean(base, 126)

def mimp_180_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 59 market impact proxy over a 252d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(6).rolling(30).mean())
    return _rolling_mean(base, 252)

def mimp_181_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 59 market impact proxy by measuring deviations from the 5d mean.
    """
    base = (volume.pct_change(6).rolling(30).mean())
    return _zscore_rolling(base, 5)

def mimp_182_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 59 market impact proxy by measuring deviations from the 21d mean.
    """
    base = (volume.pct_change(6).rolling(30).mean())
    return _zscore_rolling(base, 21)

def mimp_183_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 59 market impact proxy by measuring deviations from the 63d mean.
    """
    base = (volume.pct_change(6).rolling(30).mean())
    return _zscore_rolling(base, 63)

def mimp_184_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 59 market impact proxy by measuring deviations from the 126d mean.
    """
    base = (volume.pct_change(6).rolling(30).mean())
    return _zscore_rolling(base, 126)

def mimp_185_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 59 market impact proxy by measuring deviations from the 252d mean.
    """
    base = (volume.pct_change(6).rolling(30).mean())
    return _zscore_rolling(base, 252)

def mimp_186_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 59 market impact proxy to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = (volume.pct_change(6).rolling(30).mean())
    return _rank_pct(base, 5)

def mimp_187_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 59 market impact proxy to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = (volume.pct_change(6).rolling(30).mean())
    return _rank_pct(base, 21)

def mimp_188_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 59 market impact proxy to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = (volume.pct_change(6).rolling(30).mean())
    return _rank_pct(base, 63)

def mimp_189_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 59 market impact proxy to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = (volume.pct_change(6).rolling(30).mean())
    return _rank_pct(base, 126)

def mimp_190_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 59 market impact proxy to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = (volume.pct_change(6).rolling(30).mean())
    return _rank_pct(base, 252)

def mimp_191_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 59 market impact proxy distribution over 5d to detect tail risk or exhaustion.
    """
    base = (volume.pct_change(6).rolling(30).mean())
    return _rolling_skew(base, 5)

def mimp_192_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 59 market impact proxy distribution over 21d to detect tail risk or exhaustion.
    """
    base = (volume.pct_change(6).rolling(30).mean())
    return _rolling_skew(base, 21)

def mimp_193_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 59 market impact proxy distribution over 63d to detect tail risk or exhaustion.
    """
    base = (volume.pct_change(6).rolling(30).mean())
    return _rolling_skew(base, 63)

def mimp_194_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 59 market impact proxy distribution over 126d to detect tail risk or exhaustion.
    """
    base = (volume.pct_change(6).rolling(30).mean())
    return _rolling_skew(base, 126)

def mimp_195_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 59 market impact proxy distribution over 252d to detect tail risk or exhaustion.
    """
    base = (volume.pct_change(6).rolling(30).mean())
    return _rolling_skew(base, 252)

def mimp_196_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 59 market impact proxy over 5d to capture explosive breakdown or reversal points.
    """
    base = (volume.pct_change(6).rolling(30).mean())
    return _rolling_kurt(base, 5)

def mimp_197_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 59 market impact proxy over 21d to capture explosive breakdown or reversal points.
    """
    base = (volume.pct_change(6).rolling(30).mean())
    return _rolling_kurt(base, 21)

def mimp_198_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 59 market impact proxy over 63d to capture explosive breakdown or reversal points.
    """
    base = (volume.pct_change(6).rolling(30).mean())
    return _rolling_kurt(base, 63)

def mimp_199_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 59 market impact proxy over 126d to capture explosive breakdown or reversal points.
    """
    base = (volume.pct_change(6).rolling(30).mean())
    return _rolling_kurt(base, 126)

def mimp_200_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 59 market impact proxy over 252d to capture explosive breakdown or reversal points.
    """
    base = (volume.pct_change(6).rolling(30).mean())
    return _rolling_kurt(base, 252)

def mimp_201_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 59 market impact proxy for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = (volume.pct_change(6).rolling(30).mean())
    return _safe_div(base, _rolling_std(base, 5))

def mimp_202_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 59 market impact proxy for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = (volume.pct_change(6).rolling(30).mean())
    return _safe_div(base, _rolling_std(base, 21))

def mimp_203_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 59 market impact proxy for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = (volume.pct_change(6).rolling(30).mean())
    return _safe_div(base, _rolling_std(base, 63))

def mimp_204_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 59 market impact proxy for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = (volume.pct_change(6).rolling(30).mean())
    return _safe_div(base, _rolling_std(base, 126))

def mimp_205_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 59 market impact proxy for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = (volume.pct_change(6).rolling(30).mean())
    return _safe_div(base, _rolling_std(base, 252))

def mimp_206_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 59 market impact proxy over 5d to stabilize variance and capture exponential shifts.
    """
    base = (volume.pct_change(6).rolling(30).mean())
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def mimp_207_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 59 market impact proxy over 21d to stabilize variance and capture exponential shifts.
    """
    base = (volume.pct_change(6).rolling(30).mean())
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def mimp_208_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 59 market impact proxy over 63d to stabilize variance and capture exponential shifts.
    """
    base = (volume.pct_change(6).rolling(30).mean())
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def mimp_209_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 59 market impact proxy over 126d to stabilize variance and capture exponential shifts.
    """
    base = (volume.pct_change(6).rolling(30).mean())
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def mimp_210_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 59 market impact proxy over 252d to stabilize variance and capture exponential shifts.
    """
    base = (volume.pct_change(6).rolling(30).mean())
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def mimp_211_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 59 market impact proxy over a 5d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(7).rolling(35).mean())
    return _rolling_mean(base, 5)

def mimp_212_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 59 market impact proxy over a 21d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(7).rolling(35).mean())
    return _rolling_mean(base, 21)

def mimp_213_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 59 market impact proxy over a 63d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(7).rolling(35).mean())
    return _rolling_mean(base, 63)

def mimp_214_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 59 market impact proxy over a 126d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(7).rolling(35).mean())
    return _rolling_mean(base, 126)

def mimp_215_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 59 market impact proxy over a 252d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(7).rolling(35).mean())
    return _rolling_mean(base, 252)

def mimp_216_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 59 market impact proxy by measuring deviations from the 5d mean.
    """
    base = (volume.pct_change(7).rolling(35).mean())
    return _zscore_rolling(base, 5)

def mimp_217_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 59 market impact proxy by measuring deviations from the 21d mean.
    """
    base = (volume.pct_change(7).rolling(35).mean())
    return _zscore_rolling(base, 21)

def mimp_218_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 59 market impact proxy by measuring deviations from the 63d mean.
    """
    base = (volume.pct_change(7).rolling(35).mean())
    return _zscore_rolling(base, 63)

def mimp_219_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 59 market impact proxy by measuring deviations from the 126d mean.
    """
    base = (volume.pct_change(7).rolling(35).mean())
    return _zscore_rolling(base, 126)

def mimp_220_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 59 market impact proxy by measuring deviations from the 252d mean.
    """
    base = (volume.pct_change(7).rolling(35).mean())
    return _zscore_rolling(base, 252)

def mimp_221_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 59 market impact proxy to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = (volume.pct_change(7).rolling(35).mean())
    return _rank_pct(base, 5)

def mimp_222_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 59 market impact proxy to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = (volume.pct_change(7).rolling(35).mean())
    return _rank_pct(base, 21)

def mimp_223_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 59 market impact proxy to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = (volume.pct_change(7).rolling(35).mean())
    return _rank_pct(base, 63)

def mimp_224_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 59 market impact proxy to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = (volume.pct_change(7).rolling(35).mean())
    return _rank_pct(base, 126)

def mimp_225_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 59 market impact proxy to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = (volume.pct_change(7).rolling(35).mean())
    return _rank_pct(base, 252)
