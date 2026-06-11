"""
80_80_yield_distress — Base Features 151-225
Domain: 80_yield_distress
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

def yldd_151_rank_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 80 yield distress to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = ocf.rolling(21).std()
    return _rank_pct(base, 5)

def yldd_152_rank_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 80 yield distress to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = ocf.rolling(21).std()
    return _rank_pct(base, 21)

def yldd_153_rank_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 80 yield distress to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = ocf.rolling(21).std()
    return _rank_pct(base, 63)

def yldd_154_rank_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 80 yield distress to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = ocf.rolling(21).std()
    return _rank_pct(base, 126)

def yldd_155_rank_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 80 yield distress to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = ocf.rolling(21).std()
    return _rank_pct(base, 252)

def yldd_156_skew_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 80 yield distress distribution over 5d to detect tail risk or exhaustion.
    """
    base = ocf.rolling(21).std()
    return _rolling_skew(base, 5)

def yldd_157_skew_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 80 yield distress distribution over 21d to detect tail risk or exhaustion.
    """
    base = ocf.rolling(21).std()
    return _rolling_skew(base, 21)

def yldd_158_skew_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 80 yield distress distribution over 63d to detect tail risk or exhaustion.
    """
    base = ocf.rolling(21).std()
    return _rolling_skew(base, 63)

def yldd_159_skew_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 80 yield distress distribution over 126d to detect tail risk or exhaustion.
    """
    base = ocf.rolling(21).std()
    return _rolling_skew(base, 126)

def yldd_160_skew_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 80 yield distress distribution over 252d to detect tail risk or exhaustion.
    """
    base = ocf.rolling(21).std()
    return _rolling_skew(base, 252)

def yldd_161_kurt_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 80 yield distress over 5d to capture explosive breakdown or reversal points.
    """
    base = ocf.rolling(21).std()
    return _rolling_kurt(base, 5)

def yldd_162_kurt_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 80 yield distress over 21d to capture explosive breakdown or reversal points.
    """
    base = ocf.rolling(21).std()
    return _rolling_kurt(base, 21)

def yldd_163_kurt_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 80 yield distress over 63d to capture explosive breakdown or reversal points.
    """
    base = ocf.rolling(21).std()
    return _rolling_kurt(base, 63)

def yldd_164_kurt_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 80 yield distress over 126d to capture explosive breakdown or reversal points.
    """
    base = ocf.rolling(21).std()
    return _rolling_kurt(base, 126)

def yldd_165_kurt_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 80 yield distress over 252d to capture explosive breakdown or reversal points.
    """
    base = ocf.rolling(21).std()
    return _rolling_kurt(base, 252)

def yldd_166_voladj_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 80 yield distress for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = ocf.rolling(21).std()
    return _safe_div(base, _rolling_std(base, 5))

def yldd_167_voladj_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 80 yield distress for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = ocf.rolling(21).std()
    return _safe_div(base, _rolling_std(base, 21))

def yldd_168_voladj_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 80 yield distress for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = ocf.rolling(21).std()
    return _safe_div(base, _rolling_std(base, 63))

def yldd_169_voladj_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 80 yield distress for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = ocf.rolling(21).std()
    return _safe_div(base, _rolling_std(base, 126))

def yldd_170_voladj_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 80 yield distress for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = ocf.rolling(21).std()
    return _safe_div(base, _rolling_std(base, 252))

def yldd_171_lognorm_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 80 yield distress over 5d to stabilize variance and capture exponential shifts.
    """
    base = ocf.rolling(21).std()
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def yldd_172_lognorm_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 80 yield distress over 21d to stabilize variance and capture exponential shifts.
    """
    base = ocf.rolling(21).std()
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def yldd_173_lognorm_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 80 yield distress over 63d to stabilize variance and capture exponential shifts.
    """
    base = ocf.rolling(21).std()
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def yldd_174_lognorm_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 80 yield distress over 126d to stabilize variance and capture exponential shifts.
    """
    base = ocf.rolling(21).std()
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def yldd_175_lognorm_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 80 yield distress over 252d to stabilize variance and capture exponential shifts.
    """
    base = ocf.rolling(21).std()
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def yldd_176_lvl_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 80 yield distress over a 5d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(30)
    return _rolling_mean(base, 5)

def yldd_177_lvl_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 80 yield distress over a 21d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(30)
    return _rolling_mean(base, 21)

def yldd_178_lvl_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 80 yield distress over a 63d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(30)
    return _rolling_mean(base, 63)

def yldd_179_lvl_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 80 yield distress over a 126d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(30)
    return _rolling_mean(base, 126)

def yldd_180_lvl_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 80 yield distress over a 252d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(30)
    return _rolling_mean(base, 252)

def yldd_181_zscore_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 80 yield distress by measuring deviations from the 5d mean.
    """
    base = marketcap.pct_change(30)
    return _zscore_rolling(base, 5)

def yldd_182_zscore_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 80 yield distress by measuring deviations from the 21d mean.
    """
    base = marketcap.pct_change(30)
    return _zscore_rolling(base, 21)

def yldd_183_zscore_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 80 yield distress by measuring deviations from the 63d mean.
    """
    base = marketcap.pct_change(30)
    return _zscore_rolling(base, 63)

def yldd_184_zscore_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 80 yield distress by measuring deviations from the 126d mean.
    """
    base = marketcap.pct_change(30)
    return _zscore_rolling(base, 126)

def yldd_185_zscore_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 80 yield distress by measuring deviations from the 252d mean.
    """
    base = marketcap.pct_change(30)
    return _zscore_rolling(base, 252)

def yldd_186_rank_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 80 yield distress to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(30)
    return _rank_pct(base, 5)

def yldd_187_rank_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 80 yield distress to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(30)
    return _rank_pct(base, 21)

def yldd_188_rank_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 80 yield distress to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(30)
    return _rank_pct(base, 63)

def yldd_189_rank_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 80 yield distress to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(30)
    return _rank_pct(base, 126)

def yldd_190_rank_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 80 yield distress to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(30)
    return _rank_pct(base, 252)

def yldd_191_skew_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 80 yield distress distribution over 5d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(30)
    return _rolling_skew(base, 5)

def yldd_192_skew_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 80 yield distress distribution over 21d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(30)
    return _rolling_skew(base, 21)

def yldd_193_skew_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 80 yield distress distribution over 63d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(30)
    return _rolling_skew(base, 63)

def yldd_194_skew_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 80 yield distress distribution over 126d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(30)
    return _rolling_skew(base, 126)

def yldd_195_skew_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 80 yield distress distribution over 252d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(30)
    return _rolling_skew(base, 252)

def yldd_196_kurt_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 80 yield distress over 5d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(30)
    return _rolling_kurt(base, 5)

def yldd_197_kurt_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 80 yield distress over 21d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(30)
    return _rolling_kurt(base, 21)

def yldd_198_kurt_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 80 yield distress over 63d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(30)
    return _rolling_kurt(base, 63)

def yldd_199_kurt_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 80 yield distress over 126d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(30)
    return _rolling_kurt(base, 126)

def yldd_200_kurt_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 80 yield distress over 252d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(30)
    return _rolling_kurt(base, 252)

def yldd_201_voladj_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 80 yield distress for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(30)
    return _safe_div(base, _rolling_std(base, 5))

def yldd_202_voladj_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 80 yield distress for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(30)
    return _safe_div(base, _rolling_std(base, 21))

def yldd_203_voladj_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 80 yield distress for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(30)
    return _safe_div(base, _rolling_std(base, 63))

def yldd_204_voladj_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 80 yield distress for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(30)
    return _safe_div(base, _rolling_std(base, 126))

def yldd_205_voladj_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 80 yield distress for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(30)
    return _safe_div(base, _rolling_std(base, 252))

def yldd_206_lognorm_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 80 yield distress over 5d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(30)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def yldd_207_lognorm_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 80 yield distress over 21d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(30)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def yldd_208_lognorm_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 80 yield distress over 63d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(30)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def yldd_209_lognorm_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 80 yield distress over 126d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(30)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def yldd_210_lognorm_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 80 yield distress over 252d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(30)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def yldd_211_lvl_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 80 yield distress over a 5d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(35)
    return _rolling_mean(base, 5)

def yldd_212_lvl_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 80 yield distress over a 21d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(35)
    return _rolling_mean(base, 21)

def yldd_213_lvl_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 80 yield distress over a 63d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(35)
    return _rolling_mean(base, 63)

def yldd_214_lvl_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 80 yield distress over a 126d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(35)
    return _rolling_mean(base, 126)

def yldd_215_lvl_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 80 yield distress over a 252d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(35)
    return _rolling_mean(base, 252)

def yldd_216_zscore_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 80 yield distress by measuring deviations from the 5d mean.
    """
    base = marketcap.pct_change(35)
    return _zscore_rolling(base, 5)

def yldd_217_zscore_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 80 yield distress by measuring deviations from the 21d mean.
    """
    base = marketcap.pct_change(35)
    return _zscore_rolling(base, 21)

def yldd_218_zscore_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 80 yield distress by measuring deviations from the 63d mean.
    """
    base = marketcap.pct_change(35)
    return _zscore_rolling(base, 63)

def yldd_219_zscore_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 80 yield distress by measuring deviations from the 126d mean.
    """
    base = marketcap.pct_change(35)
    return _zscore_rolling(base, 126)

def yldd_220_zscore_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 80 yield distress by measuring deviations from the 252d mean.
    """
    base = marketcap.pct_change(35)
    return _zscore_rolling(base, 252)

def yldd_221_rank_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 80 yield distress to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(35)
    return _rank_pct(base, 5)

def yldd_222_rank_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 80 yield distress to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(35)
    return _rank_pct(base, 21)

def yldd_223_rank_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 80 yield distress to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(35)
    return _rank_pct(base, 63)

def yldd_224_rank_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 80 yield distress to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(35)
    return _rank_pct(base, 126)

def yldd_225_rank_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 80 yield distress to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(35)
    return _rank_pct(base, 252)
