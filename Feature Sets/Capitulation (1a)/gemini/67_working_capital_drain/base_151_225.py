"""
67_67_working_capital_drain — Base Features 151-225
Domain: 67_working_capital_drain
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

def wcap_151_rank_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 67 working capital drain to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = netinc / marketcap.replace(0, 1e-9)
    return _rank_pct(base, 5)

def wcap_152_rank_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 67 working capital drain to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = netinc / marketcap.replace(0, 1e-9)
    return _rank_pct(base, 21)

def wcap_153_rank_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 67 working capital drain to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = netinc / marketcap.replace(0, 1e-9)
    return _rank_pct(base, 63)

def wcap_154_rank_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 67 working capital drain to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = netinc / marketcap.replace(0, 1e-9)
    return _rank_pct(base, 126)

def wcap_155_rank_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 67 working capital drain to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = netinc / marketcap.replace(0, 1e-9)
    return _rank_pct(base, 252)

def wcap_156_skew_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 67 working capital drain distribution over 5d to detect tail risk or exhaustion.
    """
    base = netinc / marketcap.replace(0, 1e-9)
    return _rolling_skew(base, 5)

def wcap_157_skew_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 67 working capital drain distribution over 21d to detect tail risk or exhaustion.
    """
    base = netinc / marketcap.replace(0, 1e-9)
    return _rolling_skew(base, 21)

def wcap_158_skew_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 67 working capital drain distribution over 63d to detect tail risk or exhaustion.
    """
    base = netinc / marketcap.replace(0, 1e-9)
    return _rolling_skew(base, 63)

def wcap_159_skew_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 67 working capital drain distribution over 126d to detect tail risk or exhaustion.
    """
    base = netinc / marketcap.replace(0, 1e-9)
    return _rolling_skew(base, 126)

def wcap_160_skew_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 67 working capital drain distribution over 252d to detect tail risk or exhaustion.
    """
    base = netinc / marketcap.replace(0, 1e-9)
    return _rolling_skew(base, 252)

def wcap_161_kurt_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 67 working capital drain over 5d to capture explosive breakdown or reversal points.
    """
    base = netinc / marketcap.replace(0, 1e-9)
    return _rolling_kurt(base, 5)

def wcap_162_kurt_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 67 working capital drain over 21d to capture explosive breakdown or reversal points.
    """
    base = netinc / marketcap.replace(0, 1e-9)
    return _rolling_kurt(base, 21)

def wcap_163_kurt_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 67 working capital drain over 63d to capture explosive breakdown or reversal points.
    """
    base = netinc / marketcap.replace(0, 1e-9)
    return _rolling_kurt(base, 63)

def wcap_164_kurt_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 67 working capital drain over 126d to capture explosive breakdown or reversal points.
    """
    base = netinc / marketcap.replace(0, 1e-9)
    return _rolling_kurt(base, 126)

def wcap_165_kurt_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 67 working capital drain over 252d to capture explosive breakdown or reversal points.
    """
    base = netinc / marketcap.replace(0, 1e-9)
    return _rolling_kurt(base, 252)

def wcap_166_voladj_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 67 working capital drain for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = netinc / marketcap.replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 5))

def wcap_167_voladj_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 67 working capital drain for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = netinc / marketcap.replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 21))

def wcap_168_voladj_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 67 working capital drain for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = netinc / marketcap.replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 63))

def wcap_169_voladj_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 67 working capital drain for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = netinc / marketcap.replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 126))

def wcap_170_voladj_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 67 working capital drain for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = netinc / marketcap.replace(0, 1e-9)
    return _safe_div(base, _rolling_std(base, 252))

def wcap_171_lognorm_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 67 working capital drain over 5d to stabilize variance and capture exponential shifts.
    """
    base = netinc / marketcap.replace(0, 1e-9)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def wcap_172_lognorm_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 67 working capital drain over 21d to stabilize variance and capture exponential shifts.
    """
    base = netinc / marketcap.replace(0, 1e-9)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def wcap_173_lognorm_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 67 working capital drain over 63d to stabilize variance and capture exponential shifts.
    """
    base = netinc / marketcap.replace(0, 1e-9)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def wcap_174_lognorm_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 67 working capital drain over 126d to stabilize variance and capture exponential shifts.
    """
    base = netinc / marketcap.replace(0, 1e-9)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def wcap_175_lognorm_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 67 working capital drain over 252d to stabilize variance and capture exponential shifts.
    """
    base = netinc / marketcap.replace(0, 1e-9)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def wcap_176_lvl_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 67 working capital drain over a 5d horizon to identify extreme regimes.
    """
    base = opinc.pct_change(30)
    return _rolling_mean(base, 5)

def wcap_177_lvl_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 67 working capital drain over a 21d horizon to identify extreme regimes.
    """
    base = opinc.pct_change(30)
    return _rolling_mean(base, 21)

def wcap_178_lvl_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 67 working capital drain over a 63d horizon to identify extreme regimes.
    """
    base = opinc.pct_change(30)
    return _rolling_mean(base, 63)

def wcap_179_lvl_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 67 working capital drain over a 126d horizon to identify extreme regimes.
    """
    base = opinc.pct_change(30)
    return _rolling_mean(base, 126)

def wcap_180_lvl_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 67 working capital drain over a 252d horizon to identify extreme regimes.
    """
    base = opinc.pct_change(30)
    return _rolling_mean(base, 252)

def wcap_181_zscore_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 67 working capital drain by measuring deviations from the 5d mean.
    """
    base = opinc.pct_change(30)
    return _zscore_rolling(base, 5)

def wcap_182_zscore_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 67 working capital drain by measuring deviations from the 21d mean.
    """
    base = opinc.pct_change(30)
    return _zscore_rolling(base, 21)

def wcap_183_zscore_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 67 working capital drain by measuring deviations from the 63d mean.
    """
    base = opinc.pct_change(30)
    return _zscore_rolling(base, 63)

def wcap_184_zscore_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 67 working capital drain by measuring deviations from the 126d mean.
    """
    base = opinc.pct_change(30)
    return _zscore_rolling(base, 126)

def wcap_185_zscore_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 67 working capital drain by measuring deviations from the 252d mean.
    """
    base = opinc.pct_change(30)
    return _zscore_rolling(base, 252)

def wcap_186_rank_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 67 working capital drain to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = opinc.pct_change(30)
    return _rank_pct(base, 5)

def wcap_187_rank_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 67 working capital drain to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = opinc.pct_change(30)
    return _rank_pct(base, 21)

def wcap_188_rank_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 67 working capital drain to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = opinc.pct_change(30)
    return _rank_pct(base, 63)

def wcap_189_rank_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 67 working capital drain to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = opinc.pct_change(30)
    return _rank_pct(base, 126)

def wcap_190_rank_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 67 working capital drain to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = opinc.pct_change(30)
    return _rank_pct(base, 252)

def wcap_191_skew_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 67 working capital drain distribution over 5d to detect tail risk or exhaustion.
    """
    base = opinc.pct_change(30)
    return _rolling_skew(base, 5)

def wcap_192_skew_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 67 working capital drain distribution over 21d to detect tail risk or exhaustion.
    """
    base = opinc.pct_change(30)
    return _rolling_skew(base, 21)

def wcap_193_skew_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 67 working capital drain distribution over 63d to detect tail risk or exhaustion.
    """
    base = opinc.pct_change(30)
    return _rolling_skew(base, 63)

def wcap_194_skew_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 67 working capital drain distribution over 126d to detect tail risk or exhaustion.
    """
    base = opinc.pct_change(30)
    return _rolling_skew(base, 126)

def wcap_195_skew_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 67 working capital drain distribution over 252d to detect tail risk or exhaustion.
    """
    base = opinc.pct_change(30)
    return _rolling_skew(base, 252)

def wcap_196_kurt_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 67 working capital drain over 5d to capture explosive breakdown or reversal points.
    """
    base = opinc.pct_change(30)
    return _rolling_kurt(base, 5)

def wcap_197_kurt_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 67 working capital drain over 21d to capture explosive breakdown or reversal points.
    """
    base = opinc.pct_change(30)
    return _rolling_kurt(base, 21)

def wcap_198_kurt_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 67 working capital drain over 63d to capture explosive breakdown or reversal points.
    """
    base = opinc.pct_change(30)
    return _rolling_kurt(base, 63)

def wcap_199_kurt_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 67 working capital drain over 126d to capture explosive breakdown or reversal points.
    """
    base = opinc.pct_change(30)
    return _rolling_kurt(base, 126)

def wcap_200_kurt_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 67 working capital drain over 252d to capture explosive breakdown or reversal points.
    """
    base = opinc.pct_change(30)
    return _rolling_kurt(base, 252)

def wcap_201_voladj_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 67 working capital drain for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = opinc.pct_change(30)
    return _safe_div(base, _rolling_std(base, 5))

def wcap_202_voladj_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 67 working capital drain for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = opinc.pct_change(30)
    return _safe_div(base, _rolling_std(base, 21))

def wcap_203_voladj_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 67 working capital drain for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = opinc.pct_change(30)
    return _safe_div(base, _rolling_std(base, 63))

def wcap_204_voladj_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 67 working capital drain for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = opinc.pct_change(30)
    return _safe_div(base, _rolling_std(base, 126))

def wcap_205_voladj_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 67 working capital drain for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = opinc.pct_change(30)
    return _safe_div(base, _rolling_std(base, 252))

def wcap_206_lognorm_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 67 working capital drain over 5d to stabilize variance and capture exponential shifts.
    """
    base = opinc.pct_change(30)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def wcap_207_lognorm_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 67 working capital drain over 21d to stabilize variance and capture exponential shifts.
    """
    base = opinc.pct_change(30)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def wcap_208_lognorm_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 67 working capital drain over 63d to stabilize variance and capture exponential shifts.
    """
    base = opinc.pct_change(30)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def wcap_209_lognorm_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 67 working capital drain over 126d to stabilize variance and capture exponential shifts.
    """
    base = opinc.pct_change(30)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def wcap_210_lognorm_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 67 working capital drain over 252d to stabilize variance and capture exponential shifts.
    """
    base = opinc.pct_change(30)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def wcap_211_lvl_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 67 working capital drain over a 5d horizon to identify extreme regimes.
    """
    base = opinc.pct_change(35)
    return _rolling_mean(base, 5)

def wcap_212_lvl_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 67 working capital drain over a 21d horizon to identify extreme regimes.
    """
    base = opinc.pct_change(35)
    return _rolling_mean(base, 21)

def wcap_213_lvl_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 67 working capital drain over a 63d horizon to identify extreme regimes.
    """
    base = opinc.pct_change(35)
    return _rolling_mean(base, 63)

def wcap_214_lvl_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 67 working capital drain over a 126d horizon to identify extreme regimes.
    """
    base = opinc.pct_change(35)
    return _rolling_mean(base, 126)

def wcap_215_lvl_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 67 working capital drain over a 252d horizon to identify extreme regimes.
    """
    base = opinc.pct_change(35)
    return _rolling_mean(base, 252)

def wcap_216_zscore_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 67 working capital drain by measuring deviations from the 5d mean.
    """
    base = opinc.pct_change(35)
    return _zscore_rolling(base, 5)

def wcap_217_zscore_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 67 working capital drain by measuring deviations from the 21d mean.
    """
    base = opinc.pct_change(35)
    return _zscore_rolling(base, 21)

def wcap_218_zscore_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 67 working capital drain by measuring deviations from the 63d mean.
    """
    base = opinc.pct_change(35)
    return _zscore_rolling(base, 63)

def wcap_219_zscore_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 67 working capital drain by measuring deviations from the 126d mean.
    """
    base = opinc.pct_change(35)
    return _zscore_rolling(base, 126)

def wcap_220_zscore_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 67 working capital drain by measuring deviations from the 252d mean.
    """
    base = opinc.pct_change(35)
    return _zscore_rolling(base, 252)

def wcap_221_rank_5d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 67 working capital drain to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = opinc.pct_change(35)
    return _rank_pct(base, 5)

def wcap_222_rank_21d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 67 working capital drain to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = opinc.pct_change(35)
    return _rank_pct(base, 21)

def wcap_223_rank_63d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 67 working capital drain to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = opinc.pct_change(35)
    return _rank_pct(base, 63)

def wcap_224_rank_126d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 67 working capital drain to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = opinc.pct_change(35)
    return _rank_pct(base, 126)

def wcap_225_rank_252d(revenue: pd.Series, netinc: pd.Series, opinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 67 working capital drain to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = opinc.pct_change(35)
    return _rank_pct(base, 252)
