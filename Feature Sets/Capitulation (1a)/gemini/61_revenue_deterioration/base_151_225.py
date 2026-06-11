"""
61_61_revenue_deterioration — Base Features 151-225
Domain: 61_revenue_deterioration
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

def rdet_151_rank_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 61 revenue deterioration to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = fcf / marketcap.replace(0, 1e-9)
    return _rank_pct(base, 5)

def rdet_152_rank_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 61 revenue deterioration to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = fcf / marketcap.replace(0, 1e-9)
    return _rank_pct(base, 21)

def rdet_153_rank_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 61 revenue deterioration to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = fcf / marketcap.replace(0, 1e-9)
    return _rank_pct(base, 63)

def rdet_154_rank_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 61 revenue deterioration to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = fcf / marketcap.replace(0, 1e-9)
    return _rank_pct(base, 126)

def rdet_155_rank_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 61 revenue deterioration to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = fcf / marketcap.replace(0, 1e-9)
    return _rank_pct(base, 252)

def rdet_156_skew_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 61 revenue deterioration distribution over 5d to detect tail risk or exhaustion.
    """
    base = fcf / marketcap.replace(0, 1e-9)
    return _rolling_skew(base, 5)

def rdet_157_skew_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 61 revenue deterioration distribution over 21d to detect tail risk or exhaustion.
    """
    base = fcf / marketcap.replace(0, 1e-9)
    return _rolling_skew(base, 21)

def rdet_158_skew_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 61 revenue deterioration distribution over 63d to detect tail risk or exhaustion.
    """
    base = fcf / marketcap.replace(0, 1e-9)
    return _rolling_skew(base, 63)

def rdet_159_skew_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 61 revenue deterioration distribution over 126d to detect tail risk or exhaustion.
    """
    base = fcf / marketcap.replace(0, 1e-9)
    return _rolling_skew(base, 126)

def rdet_160_skew_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 61 revenue deterioration distribution over 252d to detect tail risk or exhaustion.
    """
    base = fcf / marketcap.replace(0, 1e-9)
    return _rolling_skew(base, 252)

def rdet_161_kurt_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 61 revenue deterioration over 5d to capture explosive breakdown or reversal points.
    """
    base = fcf / marketcap.replace(0, 1e-9)
    return _rolling_kurt(base, 5)

def rdet_162_kurt_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 61 revenue deterioration over 21d to capture explosive breakdown or reversal points.
    """
    base = fcf / marketcap.replace(0, 1e-9)
    return _rolling_kurt(base, 21)

def rdet_163_kurt_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 61 revenue deterioration over 63d to capture explosive breakdown or reversal points.
    """
    base = fcf / marketcap.replace(0, 1e-9)
    return _rolling_kurt(base, 63)

def rdet_164_kurt_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 61 revenue deterioration over 126d to capture explosive breakdown or reversal points.
    """
    base = fcf / marketcap.replace(0, 1e-9)
    return _rolling_kurt(base, 126)

def rdet_165_kurt_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 61 revenue deterioration over 252d to capture explosive breakdown or reversal points.
    """
    base = fcf / marketcap.replace(0, 1e-9)
    return _rolling_kurt(base, 252)

def rdet_166_voladj_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 61 revenue deterioration for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = fcf / marketcap.replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 5))

def rdet_167_voladj_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 61 revenue deterioration for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = fcf / marketcap.replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 21))

def rdet_168_voladj_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 61 revenue deterioration for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = fcf / marketcap.replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 63))

def rdet_169_voladj_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 61 revenue deterioration for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = fcf / marketcap.replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 126))

def rdet_170_voladj_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 61 revenue deterioration for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = fcf / marketcap.replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 252))

def rdet_171_lognorm_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 61 revenue deterioration over 5d to stabilize variance and capture exponential shifts.
    """
    base = fcf / marketcap.replace(0, 1e-9)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def rdet_172_lognorm_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 61 revenue deterioration over 21d to stabilize variance and capture exponential shifts.
    """
    base = fcf / marketcap.replace(0, 1e-9)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def rdet_173_lognorm_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 61 revenue deterioration over 63d to stabilize variance and capture exponential shifts.
    """
    base = fcf / marketcap.replace(0, 1e-9)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def rdet_174_lognorm_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 61 revenue deterioration over 126d to stabilize variance and capture exponential shifts.
    """
    base = fcf / marketcap.replace(0, 1e-9)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def rdet_175_lognorm_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 61 revenue deterioration over 252d to stabilize variance and capture exponential shifts.
    """
    base = fcf / marketcap.replace(0, 1e-9)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def rdet_176_lvl_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 61 revenue deterioration over a 5d horizon to identify extreme regimes.
    """
    base = revenue.pct_change(30)
    return _rolling_mean(base, 5)

def rdet_177_lvl_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 61 revenue deterioration over a 21d horizon to identify extreme regimes.
    """
    base = revenue.pct_change(30)
    return _rolling_mean(base, 21)

def rdet_178_lvl_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 61 revenue deterioration over a 63d horizon to identify extreme regimes.
    """
    base = revenue.pct_change(30)
    return _rolling_mean(base, 63)

def rdet_179_lvl_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 61 revenue deterioration over a 126d horizon to identify extreme regimes.
    """
    base = revenue.pct_change(30)
    return _rolling_mean(base, 126)

def rdet_180_lvl_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 61 revenue deterioration over a 252d horizon to identify extreme regimes.
    """
    base = revenue.pct_change(30)
    return _rolling_mean(base, 252)

def rdet_181_zscore_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 61 revenue deterioration by measuring deviations from the 5d mean.
    """
    base = revenue.pct_change(30)
    return _zscore_rolling(base, 5)

def rdet_182_zscore_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 61 revenue deterioration by measuring deviations from the 21d mean.
    """
    base = revenue.pct_change(30)
    return _zscore_rolling(base, 21)

def rdet_183_zscore_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 61 revenue deterioration by measuring deviations from the 63d mean.
    """
    base = revenue.pct_change(30)
    return _zscore_rolling(base, 63)

def rdet_184_zscore_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 61 revenue deterioration by measuring deviations from the 126d mean.
    """
    base = revenue.pct_change(30)
    return _zscore_rolling(base, 126)

def rdet_185_zscore_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 61 revenue deterioration by measuring deviations from the 252d mean.
    """
    base = revenue.pct_change(30)
    return _zscore_rolling(base, 252)

def rdet_186_rank_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 61 revenue deterioration to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = revenue.pct_change(30)
    return _rank_pct(base, 5)

def rdet_187_rank_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 61 revenue deterioration to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = revenue.pct_change(30)
    return _rank_pct(base, 21)

def rdet_188_rank_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 61 revenue deterioration to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = revenue.pct_change(30)
    return _rank_pct(base, 63)

def rdet_189_rank_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 61 revenue deterioration to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = revenue.pct_change(30)
    return _rank_pct(base, 126)

def rdet_190_rank_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 61 revenue deterioration to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = revenue.pct_change(30)
    return _rank_pct(base, 252)

def rdet_191_skew_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 61 revenue deterioration distribution over 5d to detect tail risk or exhaustion.
    """
    base = revenue.pct_change(30)
    return _rolling_skew(base, 5)

def rdet_192_skew_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 61 revenue deterioration distribution over 21d to detect tail risk or exhaustion.
    """
    base = revenue.pct_change(30)
    return _rolling_skew(base, 21)

def rdet_193_skew_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 61 revenue deterioration distribution over 63d to detect tail risk or exhaustion.
    """
    base = revenue.pct_change(30)
    return _rolling_skew(base, 63)

def rdet_194_skew_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 61 revenue deterioration distribution over 126d to detect tail risk or exhaustion.
    """
    base = revenue.pct_change(30)
    return _rolling_skew(base, 126)

def rdet_195_skew_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 61 revenue deterioration distribution over 252d to detect tail risk or exhaustion.
    """
    base = revenue.pct_change(30)
    return _rolling_skew(base, 252)

def rdet_196_kurt_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 61 revenue deterioration over 5d to capture explosive breakdown or reversal points.
    """
    base = revenue.pct_change(30)
    return _rolling_kurt(base, 5)

def rdet_197_kurt_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 61 revenue deterioration over 21d to capture explosive breakdown or reversal points.
    """
    base = revenue.pct_change(30)
    return _rolling_kurt(base, 21)

def rdet_198_kurt_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 61 revenue deterioration over 63d to capture explosive breakdown or reversal points.
    """
    base = revenue.pct_change(30)
    return _rolling_kurt(base, 63)

def rdet_199_kurt_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 61 revenue deterioration over 126d to capture explosive breakdown or reversal points.
    """
    base = revenue.pct_change(30)
    return _rolling_kurt(base, 126)

def rdet_200_kurt_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 61 revenue deterioration over 252d to capture explosive breakdown or reversal points.
    """
    base = revenue.pct_change(30)
    return _rolling_kurt(base, 252)

def rdet_201_voladj_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 61 revenue deterioration for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = revenue.pct_change(30)
    return _safe_div(base, _rolling_std(base, 5))

def rdet_202_voladj_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 61 revenue deterioration for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = revenue.pct_change(30)
    return _safe_div(base, _rolling_std(base, 21))

def rdet_203_voladj_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 61 revenue deterioration for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = revenue.pct_change(30)
    return _safe_div(base, _rolling_std(base, 63))

def rdet_204_voladj_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 61 revenue deterioration for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = revenue.pct_change(30)
    return _safe_div(base, _rolling_std(base, 126))

def rdet_205_voladj_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 61 revenue deterioration for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = revenue.pct_change(30)
    return _safe_div(base, _rolling_std(base, 252))

def rdet_206_lognorm_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 61 revenue deterioration over 5d to stabilize variance and capture exponential shifts.
    """
    base = revenue.pct_change(30)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def rdet_207_lognorm_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 61 revenue deterioration over 21d to stabilize variance and capture exponential shifts.
    """
    base = revenue.pct_change(30)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def rdet_208_lognorm_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 61 revenue deterioration over 63d to stabilize variance and capture exponential shifts.
    """
    base = revenue.pct_change(30)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def rdet_209_lognorm_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 61 revenue deterioration over 126d to stabilize variance and capture exponential shifts.
    """
    base = revenue.pct_change(30)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def rdet_210_lognorm_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 61 revenue deterioration over 252d to stabilize variance and capture exponential shifts.
    """
    base = revenue.pct_change(30)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def rdet_211_lvl_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 61 revenue deterioration over a 5d horizon to identify extreme regimes.
    """
    base = revenue.pct_change(35)
    return _rolling_mean(base, 5)

def rdet_212_lvl_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 61 revenue deterioration over a 21d horizon to identify extreme regimes.
    """
    base = revenue.pct_change(35)
    return _rolling_mean(base, 21)

def rdet_213_lvl_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 61 revenue deterioration over a 63d horizon to identify extreme regimes.
    """
    base = revenue.pct_change(35)
    return _rolling_mean(base, 63)

def rdet_214_lvl_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 61 revenue deterioration over a 126d horizon to identify extreme regimes.
    """
    base = revenue.pct_change(35)
    return _rolling_mean(base, 126)

def rdet_215_lvl_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 61 revenue deterioration over a 252d horizon to identify extreme regimes.
    """
    base = revenue.pct_change(35)
    return _rolling_mean(base, 252)

def rdet_216_zscore_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 61 revenue deterioration by measuring deviations from the 5d mean.
    """
    base = revenue.pct_change(35)
    return _zscore_rolling(base, 5)

def rdet_217_zscore_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 61 revenue deterioration by measuring deviations from the 21d mean.
    """
    base = revenue.pct_change(35)
    return _zscore_rolling(base, 21)

def rdet_218_zscore_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 61 revenue deterioration by measuring deviations from the 63d mean.
    """
    base = revenue.pct_change(35)
    return _zscore_rolling(base, 63)

def rdet_219_zscore_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 61 revenue deterioration by measuring deviations from the 126d mean.
    """
    base = revenue.pct_change(35)
    return _zscore_rolling(base, 126)

def rdet_220_zscore_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 61 revenue deterioration by measuring deviations from the 252d mean.
    """
    base = revenue.pct_change(35)
    return _zscore_rolling(base, 252)

def rdet_221_rank_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 61 revenue deterioration to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = revenue.pct_change(35)
    return _rank_pct(base, 5)

def rdet_222_rank_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 61 revenue deterioration to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = revenue.pct_change(35)
    return _rank_pct(base, 21)

def rdet_223_rank_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 61 revenue deterioration to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = revenue.pct_change(35)
    return _rank_pct(base, 63)

def rdet_224_rank_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 61 revenue deterioration to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = revenue.pct_change(35)
    return _rank_pct(base, 126)

def rdet_225_rank_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 61 revenue deterioration to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = revenue.pct_change(35)
    return _rank_pct(base, 252)
