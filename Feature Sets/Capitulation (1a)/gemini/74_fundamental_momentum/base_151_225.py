"""
74_74_fundamental_momentum — Base Features 151-225
Domain: 74_fundamental_momentum
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

def fmom_151_rank_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 74 fundamental momentum to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = ocf.rolling(21).std()
    return _rank_pct(base, 5)

def fmom_152_rank_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 74 fundamental momentum to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = ocf.rolling(21).std()
    return _rank_pct(base, 21)

def fmom_153_rank_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 74 fundamental momentum to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = ocf.rolling(21).std()
    return _rank_pct(base, 63)

def fmom_154_rank_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 74 fundamental momentum to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = ocf.rolling(21).std()
    return _rank_pct(base, 126)

def fmom_155_rank_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 74 fundamental momentum to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = ocf.rolling(21).std()
    return _rank_pct(base, 252)

def fmom_156_skew_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 74 fundamental momentum distribution over 5d to detect tail risk or exhaustion.
    """
    base = ocf.rolling(21).std()
    return _rolling_skew(base, 5)

def fmom_157_skew_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 74 fundamental momentum distribution over 21d to detect tail risk or exhaustion.
    """
    base = ocf.rolling(21).std()
    return _rolling_skew(base, 21)

def fmom_158_skew_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 74 fundamental momentum distribution over 63d to detect tail risk or exhaustion.
    """
    base = ocf.rolling(21).std()
    return _rolling_skew(base, 63)

def fmom_159_skew_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 74 fundamental momentum distribution over 126d to detect tail risk or exhaustion.
    """
    base = ocf.rolling(21).std()
    return _rolling_skew(base, 126)

def fmom_160_skew_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 74 fundamental momentum distribution over 252d to detect tail risk or exhaustion.
    """
    base = ocf.rolling(21).std()
    return _rolling_skew(base, 252)

def fmom_161_kurt_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 74 fundamental momentum over 5d to capture explosive breakdown or reversal points.
    """
    base = ocf.rolling(21).std()
    return _rolling_kurt(base, 5)

def fmom_162_kurt_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 74 fundamental momentum over 21d to capture explosive breakdown or reversal points.
    """
    base = ocf.rolling(21).std()
    return _rolling_kurt(base, 21)

def fmom_163_kurt_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 74 fundamental momentum over 63d to capture explosive breakdown or reversal points.
    """
    base = ocf.rolling(21).std()
    return _rolling_kurt(base, 63)

def fmom_164_kurt_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 74 fundamental momentum over 126d to capture explosive breakdown or reversal points.
    """
    base = ocf.rolling(21).std()
    return _rolling_kurt(base, 126)

def fmom_165_kurt_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 74 fundamental momentum over 252d to capture explosive breakdown or reversal points.
    """
    base = ocf.rolling(21).std()
    return _rolling_kurt(base, 252)

def fmom_166_voladj_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 74 fundamental momentum for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = ocf.rolling(21).std()
    return _safe_div(base, _rolling_std(base, 5))

def fmom_167_voladj_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 74 fundamental momentum for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = ocf.rolling(21).std()
    return _safe_div(base, _rolling_std(base, 21))

def fmom_168_voladj_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 74 fundamental momentum for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = ocf.rolling(21).std()
    return _safe_div(base, _rolling_std(base, 63))

def fmom_169_voladj_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 74 fundamental momentum for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = ocf.rolling(21).std()
    return _safe_div(base, _rolling_std(base, 126))

def fmom_170_voladj_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 74 fundamental momentum for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = ocf.rolling(21).std()
    return _safe_div(base, _rolling_std(base, 252))

def fmom_171_lognorm_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 74 fundamental momentum over 5d to stabilize variance and capture exponential shifts.
    """
    base = ocf.rolling(21).std()
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def fmom_172_lognorm_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 74 fundamental momentum over 21d to stabilize variance and capture exponential shifts.
    """
    base = ocf.rolling(21).std()
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def fmom_173_lognorm_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 74 fundamental momentum over 63d to stabilize variance and capture exponential shifts.
    """
    base = ocf.rolling(21).std()
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def fmom_174_lognorm_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 74 fundamental momentum over 126d to stabilize variance and capture exponential shifts.
    """
    base = ocf.rolling(21).std()
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def fmom_175_lognorm_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 74 fundamental momentum over 252d to stabilize variance and capture exponential shifts.
    """
    base = ocf.rolling(21).std()
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def fmom_176_lvl_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 74 fundamental momentum over a 5d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(30)
    return _rolling_mean(base, 5)

def fmom_177_lvl_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 74 fundamental momentum over a 21d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(30)
    return _rolling_mean(base, 21)

def fmom_178_lvl_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 74 fundamental momentum over a 63d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(30)
    return _rolling_mean(base, 63)

def fmom_179_lvl_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 74 fundamental momentum over a 126d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(30)
    return _rolling_mean(base, 126)

def fmom_180_lvl_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 74 fundamental momentum over a 252d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(30)
    return _rolling_mean(base, 252)

def fmom_181_zscore_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 74 fundamental momentum by measuring deviations from the 5d mean.
    """
    base = marketcap.pct_change(30)
    return _zscore_rolling(base, 5)

def fmom_182_zscore_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 74 fundamental momentum by measuring deviations from the 21d mean.
    """
    base = marketcap.pct_change(30)
    return _zscore_rolling(base, 21)

def fmom_183_zscore_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 74 fundamental momentum by measuring deviations from the 63d mean.
    """
    base = marketcap.pct_change(30)
    return _zscore_rolling(base, 63)

def fmom_184_zscore_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 74 fundamental momentum by measuring deviations from the 126d mean.
    """
    base = marketcap.pct_change(30)
    return _zscore_rolling(base, 126)

def fmom_185_zscore_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 74 fundamental momentum by measuring deviations from the 252d mean.
    """
    base = marketcap.pct_change(30)
    return _zscore_rolling(base, 252)

def fmom_186_rank_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 74 fundamental momentum to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(30)
    return _rank_pct(base, 5)

def fmom_187_rank_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 74 fundamental momentum to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(30)
    return _rank_pct(base, 21)

def fmom_188_rank_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 74 fundamental momentum to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(30)
    return _rank_pct(base, 63)

def fmom_189_rank_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 74 fundamental momentum to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(30)
    return _rank_pct(base, 126)

def fmom_190_rank_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 74 fundamental momentum to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(30)
    return _rank_pct(base, 252)

def fmom_191_skew_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 74 fundamental momentum distribution over 5d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(30)
    return _rolling_skew(base, 5)

def fmom_192_skew_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 74 fundamental momentum distribution over 21d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(30)
    return _rolling_skew(base, 21)

def fmom_193_skew_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 74 fundamental momentum distribution over 63d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(30)
    return _rolling_skew(base, 63)

def fmom_194_skew_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 74 fundamental momentum distribution over 126d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(30)
    return _rolling_skew(base, 126)

def fmom_195_skew_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 74 fundamental momentum distribution over 252d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(30)
    return _rolling_skew(base, 252)

def fmom_196_kurt_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 74 fundamental momentum over 5d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(30)
    return _rolling_kurt(base, 5)

def fmom_197_kurt_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 74 fundamental momentum over 21d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(30)
    return _rolling_kurt(base, 21)

def fmom_198_kurt_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 74 fundamental momentum over 63d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(30)
    return _rolling_kurt(base, 63)

def fmom_199_kurt_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 74 fundamental momentum over 126d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(30)
    return _rolling_kurt(base, 126)

def fmom_200_kurt_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 74 fundamental momentum over 252d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(30)
    return _rolling_kurt(base, 252)

def fmom_201_voladj_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 74 fundamental momentum for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(30)
    return _safe_div(base, _rolling_std(base, 5))

def fmom_202_voladj_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 74 fundamental momentum for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(30)
    return _safe_div(base, _rolling_std(base, 21))

def fmom_203_voladj_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 74 fundamental momentum for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(30)
    return _safe_div(base, _rolling_std(base, 63))

def fmom_204_voladj_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 74 fundamental momentum for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(30)
    return _safe_div(base, _rolling_std(base, 126))

def fmom_205_voladj_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 74 fundamental momentum for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(30)
    return _safe_div(base, _rolling_std(base, 252))

def fmom_206_lognorm_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 74 fundamental momentum over 5d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(30)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def fmom_207_lognorm_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 74 fundamental momentum over 21d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(30)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def fmom_208_lognorm_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 74 fundamental momentum over 63d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(30)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def fmom_209_lognorm_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 74 fundamental momentum over 126d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(30)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def fmom_210_lognorm_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 74 fundamental momentum over 252d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(30)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def fmom_211_lvl_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 74 fundamental momentum over a 5d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(35)
    return _rolling_mean(base, 5)

def fmom_212_lvl_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 74 fundamental momentum over a 21d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(35)
    return _rolling_mean(base, 21)

def fmom_213_lvl_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 74 fundamental momentum over a 63d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(35)
    return _rolling_mean(base, 63)

def fmom_214_lvl_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 74 fundamental momentum over a 126d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(35)
    return _rolling_mean(base, 126)

def fmom_215_lvl_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 74 fundamental momentum over a 252d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(35)
    return _rolling_mean(base, 252)

def fmom_216_zscore_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 74 fundamental momentum by measuring deviations from the 5d mean.
    """
    base = marketcap.pct_change(35)
    return _zscore_rolling(base, 5)

def fmom_217_zscore_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 74 fundamental momentum by measuring deviations from the 21d mean.
    """
    base = marketcap.pct_change(35)
    return _zscore_rolling(base, 21)

def fmom_218_zscore_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 74 fundamental momentum by measuring deviations from the 63d mean.
    """
    base = marketcap.pct_change(35)
    return _zscore_rolling(base, 63)

def fmom_219_zscore_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 74 fundamental momentum by measuring deviations from the 126d mean.
    """
    base = marketcap.pct_change(35)
    return _zscore_rolling(base, 126)

def fmom_220_zscore_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 74 fundamental momentum by measuring deviations from the 252d mean.
    """
    base = marketcap.pct_change(35)
    return _zscore_rolling(base, 252)

def fmom_221_rank_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 74 fundamental momentum to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(35)
    return _rank_pct(base, 5)

def fmom_222_rank_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 74 fundamental momentum to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(35)
    return _rank_pct(base, 21)

def fmom_223_rank_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 74 fundamental momentum to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(35)
    return _rank_pct(base, 63)

def fmom_224_rank_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 74 fundamental momentum to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(35)
    return _rank_pct(base, 126)

def fmom_225_rank_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 74 fundamental momentum to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(35)
    return _rank_pct(base, 252)
