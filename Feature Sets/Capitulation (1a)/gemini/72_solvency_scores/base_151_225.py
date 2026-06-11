"""
72_72_solvency_scores — Base Features 151-225
Domain: 72_solvency_scores
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

def solv_151_rank_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 72 solvency scores to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = ocf.rolling(21).std()
    return _rank_pct(base, 5)

def solv_152_rank_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 72 solvency scores to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = ocf.rolling(21).std()
    return _rank_pct(base, 21)

def solv_153_rank_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 72 solvency scores to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = ocf.rolling(21).std()
    return _rank_pct(base, 63)

def solv_154_rank_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 72 solvency scores to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = ocf.rolling(21).std()
    return _rank_pct(base, 126)

def solv_155_rank_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 72 solvency scores to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = ocf.rolling(21).std()
    return _rank_pct(base, 252)

def solv_156_skew_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 72 solvency scores distribution over 5d to detect tail risk or exhaustion.
    """
    base = ocf.rolling(21).std()
    return _rolling_skew(base, 5)

def solv_157_skew_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 72 solvency scores distribution over 21d to detect tail risk or exhaustion.
    """
    base = ocf.rolling(21).std()
    return _rolling_skew(base, 21)

def solv_158_skew_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 72 solvency scores distribution over 63d to detect tail risk or exhaustion.
    """
    base = ocf.rolling(21).std()
    return _rolling_skew(base, 63)

def solv_159_skew_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 72 solvency scores distribution over 126d to detect tail risk or exhaustion.
    """
    base = ocf.rolling(21).std()
    return _rolling_skew(base, 126)

def solv_160_skew_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 72 solvency scores distribution over 252d to detect tail risk or exhaustion.
    """
    base = ocf.rolling(21).std()
    return _rolling_skew(base, 252)

def solv_161_kurt_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 72 solvency scores over 5d to capture explosive breakdown or reversal points.
    """
    base = ocf.rolling(21).std()
    return _rolling_kurt(base, 5)

def solv_162_kurt_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 72 solvency scores over 21d to capture explosive breakdown or reversal points.
    """
    base = ocf.rolling(21).std()
    return _rolling_kurt(base, 21)

def solv_163_kurt_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 72 solvency scores over 63d to capture explosive breakdown or reversal points.
    """
    base = ocf.rolling(21).std()
    return _rolling_kurt(base, 63)

def solv_164_kurt_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 72 solvency scores over 126d to capture explosive breakdown or reversal points.
    """
    base = ocf.rolling(21).std()
    return _rolling_kurt(base, 126)

def solv_165_kurt_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 72 solvency scores over 252d to capture explosive breakdown or reversal points.
    """
    base = ocf.rolling(21).std()
    return _rolling_kurt(base, 252)

def solv_166_voladj_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 72 solvency scores for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = ocf.rolling(21).std()
    return _safe_div(base, _rolling_std(base, 5))

def solv_167_voladj_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 72 solvency scores for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = ocf.rolling(21).std()
    return _safe_div(base, _rolling_std(base, 21))

def solv_168_voladj_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 72 solvency scores for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = ocf.rolling(21).std()
    return _safe_div(base, _rolling_std(base, 63))

def solv_169_voladj_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 72 solvency scores for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = ocf.rolling(21).std()
    return _safe_div(base, _rolling_std(base, 126))

def solv_170_voladj_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 72 solvency scores for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = ocf.rolling(21).std()
    return _safe_div(base, _rolling_std(base, 252))

def solv_171_lognorm_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 72 solvency scores over 5d to stabilize variance and capture exponential shifts.
    """
    base = ocf.rolling(21).std()
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def solv_172_lognorm_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 72 solvency scores over 21d to stabilize variance and capture exponential shifts.
    """
    base = ocf.rolling(21).std()
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def solv_173_lognorm_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 72 solvency scores over 63d to stabilize variance and capture exponential shifts.
    """
    base = ocf.rolling(21).std()
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def solv_174_lognorm_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 72 solvency scores over 126d to stabilize variance and capture exponential shifts.
    """
    base = ocf.rolling(21).std()
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def solv_175_lognorm_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 72 solvency scores over 252d to stabilize variance and capture exponential shifts.
    """
    base = ocf.rolling(21).std()
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def solv_176_lvl_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 72 solvency scores over a 5d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(30)
    return _rolling_mean(base, 5)

def solv_177_lvl_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 72 solvency scores over a 21d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(30)
    return _rolling_mean(base, 21)

def solv_178_lvl_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 72 solvency scores over a 63d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(30)
    return _rolling_mean(base, 63)

def solv_179_lvl_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 72 solvency scores over a 126d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(30)
    return _rolling_mean(base, 126)

def solv_180_lvl_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 72 solvency scores over a 252d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(30)
    return _rolling_mean(base, 252)

def solv_181_zscore_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 72 solvency scores by measuring deviations from the 5d mean.
    """
    base = marketcap.pct_change(30)
    return _zscore_rolling(base, 5)

def solv_182_zscore_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 72 solvency scores by measuring deviations from the 21d mean.
    """
    base = marketcap.pct_change(30)
    return _zscore_rolling(base, 21)

def solv_183_zscore_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 72 solvency scores by measuring deviations from the 63d mean.
    """
    base = marketcap.pct_change(30)
    return _zscore_rolling(base, 63)

def solv_184_zscore_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 72 solvency scores by measuring deviations from the 126d mean.
    """
    base = marketcap.pct_change(30)
    return _zscore_rolling(base, 126)

def solv_185_zscore_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 72 solvency scores by measuring deviations from the 252d mean.
    """
    base = marketcap.pct_change(30)
    return _zscore_rolling(base, 252)

def solv_186_rank_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 72 solvency scores to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(30)
    return _rank_pct(base, 5)

def solv_187_rank_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 72 solvency scores to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(30)
    return _rank_pct(base, 21)

def solv_188_rank_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 72 solvency scores to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(30)
    return _rank_pct(base, 63)

def solv_189_rank_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 72 solvency scores to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(30)
    return _rank_pct(base, 126)

def solv_190_rank_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 72 solvency scores to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(30)
    return _rank_pct(base, 252)

def solv_191_skew_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 72 solvency scores distribution over 5d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(30)
    return _rolling_skew(base, 5)

def solv_192_skew_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 72 solvency scores distribution over 21d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(30)
    return _rolling_skew(base, 21)

def solv_193_skew_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 72 solvency scores distribution over 63d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(30)
    return _rolling_skew(base, 63)

def solv_194_skew_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 72 solvency scores distribution over 126d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(30)
    return _rolling_skew(base, 126)

def solv_195_skew_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 72 solvency scores distribution over 252d to detect tail risk or exhaustion.
    """
    base = marketcap.pct_change(30)
    return _rolling_skew(base, 252)

def solv_196_kurt_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 72 solvency scores over 5d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(30)
    return _rolling_kurt(base, 5)

def solv_197_kurt_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 72 solvency scores over 21d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(30)
    return _rolling_kurt(base, 21)

def solv_198_kurt_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 72 solvency scores over 63d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(30)
    return _rolling_kurt(base, 63)

def solv_199_kurt_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 72 solvency scores over 126d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(30)
    return _rolling_kurt(base, 126)

def solv_200_kurt_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 72 solvency scores over 252d to capture explosive breakdown or reversal points.
    """
    base = marketcap.pct_change(30)
    return _rolling_kurt(base, 252)

def solv_201_voladj_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 72 solvency scores for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(30)
    return _safe_div(base, _rolling_std(base, 5))

def solv_202_voladj_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 72 solvency scores for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(30)
    return _safe_div(base, _rolling_std(base, 21))

def solv_203_voladj_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 72 solvency scores for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(30)
    return _safe_div(base, _rolling_std(base, 63))

def solv_204_voladj_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 72 solvency scores for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(30)
    return _safe_div(base, _rolling_std(base, 126))

def solv_205_voladj_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 72 solvency scores for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap.pct_change(30)
    return _safe_div(base, _rolling_std(base, 252))

def solv_206_lognorm_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 72 solvency scores over 5d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(30)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def solv_207_lognorm_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 72 solvency scores over 21d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(30)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def solv_208_lognorm_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 72 solvency scores over 63d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(30)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def solv_209_lognorm_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 72 solvency scores over 126d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(30)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def solv_210_lognorm_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 72 solvency scores over 252d to stabilize variance and capture exponential shifts.
    """
    base = marketcap.pct_change(30)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def solv_211_lvl_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 72 solvency scores over a 5d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(35)
    return _rolling_mean(base, 5)

def solv_212_lvl_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 72 solvency scores over a 21d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(35)
    return _rolling_mean(base, 21)

def solv_213_lvl_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 72 solvency scores over a 63d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(35)
    return _rolling_mean(base, 63)

def solv_214_lvl_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 72 solvency scores over a 126d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(35)
    return _rolling_mean(base, 126)

def solv_215_lvl_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 72 solvency scores over a 252d horizon to identify extreme regimes.
    """
    base = marketcap.pct_change(35)
    return _rolling_mean(base, 252)

def solv_216_zscore_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 72 solvency scores by measuring deviations from the 5d mean.
    """
    base = marketcap.pct_change(35)
    return _zscore_rolling(base, 5)

def solv_217_zscore_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 72 solvency scores by measuring deviations from the 21d mean.
    """
    base = marketcap.pct_change(35)
    return _zscore_rolling(base, 21)

def solv_218_zscore_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 72 solvency scores by measuring deviations from the 63d mean.
    """
    base = marketcap.pct_change(35)
    return _zscore_rolling(base, 63)

def solv_219_zscore_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 72 solvency scores by measuring deviations from the 126d mean.
    """
    base = marketcap.pct_change(35)
    return _zscore_rolling(base, 126)

def solv_220_zscore_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 72 solvency scores by measuring deviations from the 252d mean.
    """
    base = marketcap.pct_change(35)
    return _zscore_rolling(base, 252)

def solv_221_rank_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 72 solvency scores to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(35)
    return _rank_pct(base, 5)

def solv_222_rank_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 72 solvency scores to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(35)
    return _rank_pct(base, 21)

def solv_223_rank_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 72 solvency scores to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(35)
    return _rank_pct(base, 63)

def solv_224_rank_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 72 solvency scores to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(35)
    return _rank_pct(base, 126)

def solv_225_rank_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 72 solvency scores to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = marketcap.pct_change(35)
    return _rank_pct(base, 252)
