"""
63_63_cash_burn — Base Features 151-225
Domain: 63_cash_burn
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

def cbrn_151_rank_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 63 cash burn to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = fcf / marketcap.replace(0, 1e-9)
    return _rank_pct(base, 5)

def cbrn_152_rank_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 63 cash burn to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = fcf / marketcap.replace(0, 1e-9)
    return _rank_pct(base, 21)

def cbrn_153_rank_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 63 cash burn to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = fcf / marketcap.replace(0, 1e-9)
    return _rank_pct(base, 63)

def cbrn_154_rank_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 63 cash burn to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = fcf / marketcap.replace(0, 1e-9)
    return _rank_pct(base, 126)

def cbrn_155_rank_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 63 cash burn to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = fcf / marketcap.replace(0, 1e-9)
    return _rank_pct(base, 252)

def cbrn_156_skew_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 63 cash burn distribution over 5d to detect tail risk or exhaustion.
    """
    base = fcf / marketcap.replace(0, 1e-9)
    return _rolling_skew(base, 5)

def cbrn_157_skew_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 63 cash burn distribution over 21d to detect tail risk or exhaustion.
    """
    base = fcf / marketcap.replace(0, 1e-9)
    return _rolling_skew(base, 21)

def cbrn_158_skew_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 63 cash burn distribution over 63d to detect tail risk or exhaustion.
    """
    base = fcf / marketcap.replace(0, 1e-9)
    return _rolling_skew(base, 63)

def cbrn_159_skew_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 63 cash burn distribution over 126d to detect tail risk or exhaustion.
    """
    base = fcf / marketcap.replace(0, 1e-9)
    return _rolling_skew(base, 126)

def cbrn_160_skew_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 63 cash burn distribution over 252d to detect tail risk or exhaustion.
    """
    base = fcf / marketcap.replace(0, 1e-9)
    return _rolling_skew(base, 252)

def cbrn_161_kurt_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 63 cash burn over 5d to capture explosive breakdown or reversal points.
    """
    base = fcf / marketcap.replace(0, 1e-9)
    return _rolling_kurt(base, 5)

def cbrn_162_kurt_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 63 cash burn over 21d to capture explosive breakdown or reversal points.
    """
    base = fcf / marketcap.replace(0, 1e-9)
    return _rolling_kurt(base, 21)

def cbrn_163_kurt_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 63 cash burn over 63d to capture explosive breakdown or reversal points.
    """
    base = fcf / marketcap.replace(0, 1e-9)
    return _rolling_kurt(base, 63)

def cbrn_164_kurt_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 63 cash burn over 126d to capture explosive breakdown or reversal points.
    """
    base = fcf / marketcap.replace(0, 1e-9)
    return _rolling_kurt(base, 126)

def cbrn_165_kurt_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 63 cash burn over 252d to capture explosive breakdown or reversal points.
    """
    base = fcf / marketcap.replace(0, 1e-9)
    return _rolling_kurt(base, 252)

def cbrn_166_voladj_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 63 cash burn for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = fcf / marketcap.replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 5))

def cbrn_167_voladj_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 63 cash burn for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = fcf / marketcap.replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 21))

def cbrn_168_voladj_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 63 cash burn for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = fcf / marketcap.replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 63))

def cbrn_169_voladj_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 63 cash burn for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = fcf / marketcap.replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 126))

def cbrn_170_voladj_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 63 cash burn for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = fcf / marketcap.replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 252))

def cbrn_171_lognorm_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 63 cash burn over 5d to stabilize variance and capture exponential shifts.
    """
    base = fcf / marketcap.replace(0, 1e-9)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def cbrn_172_lognorm_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 63 cash burn over 21d to stabilize variance and capture exponential shifts.
    """
    base = fcf / marketcap.replace(0, 1e-9)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def cbrn_173_lognorm_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 63 cash burn over 63d to stabilize variance and capture exponential shifts.
    """
    base = fcf / marketcap.replace(0, 1e-9)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def cbrn_174_lognorm_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 63 cash burn over 126d to stabilize variance and capture exponential shifts.
    """
    base = fcf / marketcap.replace(0, 1e-9)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def cbrn_175_lognorm_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 63 cash burn over 252d to stabilize variance and capture exponential shifts.
    """
    base = fcf / marketcap.replace(0, 1e-9)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def cbrn_176_lvl_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 63 cash burn over a 5d horizon to identify extreme regimes.
    """
    base = revenue.pct_change(30)
    return _rolling_mean(base, 5)

def cbrn_177_lvl_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 63 cash burn over a 21d horizon to identify extreme regimes.
    """
    base = revenue.pct_change(30)
    return _rolling_mean(base, 21)

def cbrn_178_lvl_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 63 cash burn over a 63d horizon to identify extreme regimes.
    """
    base = revenue.pct_change(30)
    return _rolling_mean(base, 63)

def cbrn_179_lvl_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 63 cash burn over a 126d horizon to identify extreme regimes.
    """
    base = revenue.pct_change(30)
    return _rolling_mean(base, 126)

def cbrn_180_lvl_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 63 cash burn over a 252d horizon to identify extreme regimes.
    """
    base = revenue.pct_change(30)
    return _rolling_mean(base, 252)

def cbrn_181_zscore_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 63 cash burn by measuring deviations from the 5d mean.
    """
    base = revenue.pct_change(30)
    return _zscore_rolling(base, 5)

def cbrn_182_zscore_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 63 cash burn by measuring deviations from the 21d mean.
    """
    base = revenue.pct_change(30)
    return _zscore_rolling(base, 21)

def cbrn_183_zscore_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 63 cash burn by measuring deviations from the 63d mean.
    """
    base = revenue.pct_change(30)
    return _zscore_rolling(base, 63)

def cbrn_184_zscore_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 63 cash burn by measuring deviations from the 126d mean.
    """
    base = revenue.pct_change(30)
    return _zscore_rolling(base, 126)

def cbrn_185_zscore_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 63 cash burn by measuring deviations from the 252d mean.
    """
    base = revenue.pct_change(30)
    return _zscore_rolling(base, 252)

def cbrn_186_rank_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 63 cash burn to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = revenue.pct_change(30)
    return _rank_pct(base, 5)

def cbrn_187_rank_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 63 cash burn to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = revenue.pct_change(30)
    return _rank_pct(base, 21)

def cbrn_188_rank_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 63 cash burn to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = revenue.pct_change(30)
    return _rank_pct(base, 63)

def cbrn_189_rank_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 63 cash burn to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = revenue.pct_change(30)
    return _rank_pct(base, 126)

def cbrn_190_rank_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 63 cash burn to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = revenue.pct_change(30)
    return _rank_pct(base, 252)

def cbrn_191_skew_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 63 cash burn distribution over 5d to detect tail risk or exhaustion.
    """
    base = revenue.pct_change(30)
    return _rolling_skew(base, 5)

def cbrn_192_skew_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 63 cash burn distribution over 21d to detect tail risk or exhaustion.
    """
    base = revenue.pct_change(30)
    return _rolling_skew(base, 21)

def cbrn_193_skew_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 63 cash burn distribution over 63d to detect tail risk or exhaustion.
    """
    base = revenue.pct_change(30)
    return _rolling_skew(base, 63)

def cbrn_194_skew_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 63 cash burn distribution over 126d to detect tail risk or exhaustion.
    """
    base = revenue.pct_change(30)
    return _rolling_skew(base, 126)

def cbrn_195_skew_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 63 cash burn distribution over 252d to detect tail risk or exhaustion.
    """
    base = revenue.pct_change(30)
    return _rolling_skew(base, 252)

def cbrn_196_kurt_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 63 cash burn over 5d to capture explosive breakdown or reversal points.
    """
    base = revenue.pct_change(30)
    return _rolling_kurt(base, 5)

def cbrn_197_kurt_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 63 cash burn over 21d to capture explosive breakdown or reversal points.
    """
    base = revenue.pct_change(30)
    return _rolling_kurt(base, 21)

def cbrn_198_kurt_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 63 cash burn over 63d to capture explosive breakdown or reversal points.
    """
    base = revenue.pct_change(30)
    return _rolling_kurt(base, 63)

def cbrn_199_kurt_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 63 cash burn over 126d to capture explosive breakdown or reversal points.
    """
    base = revenue.pct_change(30)
    return _rolling_kurt(base, 126)

def cbrn_200_kurt_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 63 cash burn over 252d to capture explosive breakdown or reversal points.
    """
    base = revenue.pct_change(30)
    return _rolling_kurt(base, 252)

def cbrn_201_voladj_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 63 cash burn for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = revenue.pct_change(30)
    return _safe_div(base, _rolling_std(base, 5))

def cbrn_202_voladj_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 63 cash burn for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = revenue.pct_change(30)
    return _safe_div(base, _rolling_std(base, 21))

def cbrn_203_voladj_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 63 cash burn for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = revenue.pct_change(30)
    return _safe_div(base, _rolling_std(base, 63))

def cbrn_204_voladj_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 63 cash burn for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = revenue.pct_change(30)
    return _safe_div(base, _rolling_std(base, 126))

def cbrn_205_voladj_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 63 cash burn for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = revenue.pct_change(30)
    return _safe_div(base, _rolling_std(base, 252))

def cbrn_206_lognorm_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 63 cash burn over 5d to stabilize variance and capture exponential shifts.
    """
    base = revenue.pct_change(30)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def cbrn_207_lognorm_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 63 cash burn over 21d to stabilize variance and capture exponential shifts.
    """
    base = revenue.pct_change(30)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def cbrn_208_lognorm_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 63 cash burn over 63d to stabilize variance and capture exponential shifts.
    """
    base = revenue.pct_change(30)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def cbrn_209_lognorm_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 63 cash burn over 126d to stabilize variance and capture exponential shifts.
    """
    base = revenue.pct_change(30)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def cbrn_210_lognorm_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 63 cash burn over 252d to stabilize variance and capture exponential shifts.
    """
    base = revenue.pct_change(30)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def cbrn_211_lvl_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 63 cash burn over a 5d horizon to identify extreme regimes.
    """
    base = revenue.pct_change(35)
    return _rolling_mean(base, 5)

def cbrn_212_lvl_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 63 cash burn over a 21d horizon to identify extreme regimes.
    """
    base = revenue.pct_change(35)
    return _rolling_mean(base, 21)

def cbrn_213_lvl_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 63 cash burn over a 63d horizon to identify extreme regimes.
    """
    base = revenue.pct_change(35)
    return _rolling_mean(base, 63)

def cbrn_214_lvl_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 63 cash burn over a 126d horizon to identify extreme regimes.
    """
    base = revenue.pct_change(35)
    return _rolling_mean(base, 126)

def cbrn_215_lvl_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 63 cash burn over a 252d horizon to identify extreme regimes.
    """
    base = revenue.pct_change(35)
    return _rolling_mean(base, 252)

def cbrn_216_zscore_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 63 cash burn by measuring deviations from the 5d mean.
    """
    base = revenue.pct_change(35)
    return _zscore_rolling(base, 5)

def cbrn_217_zscore_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 63 cash burn by measuring deviations from the 21d mean.
    """
    base = revenue.pct_change(35)
    return _zscore_rolling(base, 21)

def cbrn_218_zscore_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 63 cash burn by measuring deviations from the 63d mean.
    """
    base = revenue.pct_change(35)
    return _zscore_rolling(base, 63)

def cbrn_219_zscore_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 63 cash burn by measuring deviations from the 126d mean.
    """
    base = revenue.pct_change(35)
    return _zscore_rolling(base, 126)

def cbrn_220_zscore_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 63 cash burn by measuring deviations from the 252d mean.
    """
    base = revenue.pct_change(35)
    return _zscore_rolling(base, 252)

def cbrn_221_rank_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 63 cash burn to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = revenue.pct_change(35)
    return _rank_pct(base, 5)

def cbrn_222_rank_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 63 cash burn to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = revenue.pct_change(35)
    return _rank_pct(base, 21)

def cbrn_223_rank_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 63 cash burn to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = revenue.pct_change(35)
    return _rank_pct(base, 63)

def cbrn_224_rank_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 63 cash burn to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = revenue.pct_change(35)
    return _rank_pct(base, 126)

def cbrn_225_rank_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 63 cash burn to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = revenue.pct_change(35)
    return _rank_pct(base, 252)
