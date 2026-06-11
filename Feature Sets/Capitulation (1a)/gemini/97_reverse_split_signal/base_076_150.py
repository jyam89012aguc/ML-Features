"""
97_97_reverse_split_signal — Base Features 076-150
Domain: 97_reverse_split_signal
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

def rvrs_076_zscore_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 97 reverse split signal by measuring deviations from the 5d mean.
    """
    base = _safe_div(assets - liabs, assets)
    return _zscore_rolling(base, 5)

def rvrs_077_zscore_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 97 reverse split signal by measuring deviations from the 21d mean.
    """
    base = _safe_div(assets - liabs, assets)
    return _zscore_rolling(base, 21)

def rvrs_078_zscore_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 97 reverse split signal by measuring deviations from the 63d mean.
    """
    base = _safe_div(assets - liabs, assets)
    return _zscore_rolling(base, 63)

def rvrs_079_zscore_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 97 reverse split signal by measuring deviations from the 126d mean.
    """
    base = _safe_div(assets - liabs, assets)
    return _zscore_rolling(base, 126)

def rvrs_080_zscore_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 97 reverse split signal by measuring deviations from the 252d mean.
    """
    base = _safe_div(assets - liabs, assets)
    return _zscore_rolling(base, 252)

def rvrs_081_rank_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 97 reverse split signal to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = _safe_div(assets - liabs, assets)
    return _rank_pct(base, 5)

def rvrs_082_rank_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 97 reverse split signal to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = _safe_div(assets - liabs, assets)
    return _rank_pct(base, 21)

def rvrs_083_rank_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 97 reverse split signal to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = _safe_div(assets - liabs, assets)
    return _rank_pct(base, 63)

def rvrs_084_rank_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 97 reverse split signal to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = _safe_div(assets - liabs, assets)
    return _rank_pct(base, 126)

def rvrs_085_rank_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 97 reverse split signal to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = _safe_div(assets - liabs, assets)
    return _rank_pct(base, 252)

def rvrs_086_skew_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 97 reverse split signal distribution over 5d to detect tail risk or exhaustion.
    """
    base = _safe_div(assets - liabs, assets)
    return _rolling_skew(base, 5)

def rvrs_087_skew_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 97 reverse split signal distribution over 21d to detect tail risk or exhaustion.
    """
    base = _safe_div(assets - liabs, assets)
    return _rolling_skew(base, 21)

def rvrs_088_skew_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 97 reverse split signal distribution over 63d to detect tail risk or exhaustion.
    """
    base = _safe_div(assets - liabs, assets)
    return _rolling_skew(base, 63)

def rvrs_089_skew_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 97 reverse split signal distribution over 126d to detect tail risk or exhaustion.
    """
    base = _safe_div(assets - liabs, assets)
    return _rolling_skew(base, 126)

def rvrs_090_skew_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 97 reverse split signal distribution over 252d to detect tail risk or exhaustion.
    """
    base = _safe_div(assets - liabs, assets)
    return _rolling_skew(base, 252)

def rvrs_091_kurt_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 97 reverse split signal over 5d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(assets - liabs, assets)
    return _rolling_kurt(base, 5)

def rvrs_092_kurt_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 97 reverse split signal over 21d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(assets - liabs, assets)
    return _rolling_kurt(base, 21)

def rvrs_093_kurt_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 97 reverse split signal over 63d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(assets - liabs, assets)
    return _rolling_kurt(base, 63)

def rvrs_094_kurt_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 97 reverse split signal over 126d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(assets - liabs, assets)
    return _rolling_kurt(base, 126)

def rvrs_095_kurt_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 97 reverse split signal over 252d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(assets - liabs, assets)
    return _rolling_kurt(base, 252)

def rvrs_096_voladj_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 97 reverse split signal for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(assets - liabs, assets)
    return _safe_div(base, _rolling_std(base, 5))

def rvrs_097_voladj_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 97 reverse split signal for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(assets - liabs, assets)
    return _safe_div(base, _rolling_std(base, 21))

def rvrs_098_voladj_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 97 reverse split signal for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(assets - liabs, assets)
    return _safe_div(base, _rolling_std(base, 63))

def rvrs_099_voladj_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 97 reverse split signal for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(assets - liabs, assets)
    return _safe_div(base, _rolling_std(base, 126))

def rvrs_100_voladj_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 97 reverse split signal for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(assets - liabs, assets)
    return _safe_div(base, _rolling_std(base, 252))

def rvrs_101_lognorm_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 97 reverse split signal over 5d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(assets - liabs, assets)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def rvrs_102_lognorm_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 97 reverse split signal over 21d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(assets - liabs, assets)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def rvrs_103_lognorm_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 97 reverse split signal over 63d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(assets - liabs, assets)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def rvrs_104_lognorm_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 97 reverse split signal over 126d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(assets - liabs, assets)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def rvrs_105_lognorm_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 97 reverse split signal over 252d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(assets - liabs, assets)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def rvrs_106_lvl_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 97 reverse split signal over a 5d horizon to identify extreme regimes.
    """
    base = marketcap
    return _rolling_mean(base, 5)

def rvrs_107_lvl_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 97 reverse split signal over a 21d horizon to identify extreme regimes.
    """
    base = marketcap
    return _rolling_mean(base, 21)

def rvrs_108_lvl_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 97 reverse split signal over a 63d horizon to identify extreme regimes.
    """
    base = marketcap
    return _rolling_mean(base, 63)

def rvrs_109_lvl_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 97 reverse split signal over a 126d horizon to identify extreme regimes.
    """
    base = marketcap
    return _rolling_mean(base, 126)

def rvrs_110_lvl_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 97 reverse split signal over a 252d horizon to identify extreme regimes.
    """
    base = marketcap
    return _rolling_mean(base, 252)

def rvrs_111_zscore_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 97 reverse split signal by measuring deviations from the 5d mean.
    """
    base = marketcap
    return _zscore_rolling(base, 5)

def rvrs_112_zscore_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 97 reverse split signal by measuring deviations from the 21d mean.
    """
    base = marketcap
    return _zscore_rolling(base, 21)

def rvrs_113_zscore_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 97 reverse split signal by measuring deviations from the 63d mean.
    """
    base = marketcap
    return _zscore_rolling(base, 63)

def rvrs_114_zscore_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 97 reverse split signal by measuring deviations from the 126d mean.
    """
    base = marketcap
    return _zscore_rolling(base, 126)

def rvrs_115_zscore_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 97 reverse split signal by measuring deviations from the 252d mean.
    """
    base = marketcap
    return _zscore_rolling(base, 252)

def rvrs_116_rank_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 97 reverse split signal to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = marketcap
    return _rank_pct(base, 5)

def rvrs_117_rank_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 97 reverse split signal to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = marketcap
    return _rank_pct(base, 21)

def rvrs_118_rank_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 97 reverse split signal to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = marketcap
    return _rank_pct(base, 63)

def rvrs_119_rank_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 97 reverse split signal to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = marketcap
    return _rank_pct(base, 126)

def rvrs_120_rank_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 97 reverse split signal to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = marketcap
    return _rank_pct(base, 252)

def rvrs_121_skew_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 97 reverse split signal distribution over 5d to detect tail risk or exhaustion.
    """
    base = marketcap
    return _rolling_skew(base, 5)

def rvrs_122_skew_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 97 reverse split signal distribution over 21d to detect tail risk or exhaustion.
    """
    base = marketcap
    return _rolling_skew(base, 21)

def rvrs_123_skew_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 97 reverse split signal distribution over 63d to detect tail risk or exhaustion.
    """
    base = marketcap
    return _rolling_skew(base, 63)

def rvrs_124_skew_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 97 reverse split signal distribution over 126d to detect tail risk or exhaustion.
    """
    base = marketcap
    return _rolling_skew(base, 126)

def rvrs_125_skew_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 97 reverse split signal distribution over 252d to detect tail risk or exhaustion.
    """
    base = marketcap
    return _rolling_skew(base, 252)

def rvrs_126_kurt_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 97 reverse split signal over 5d to capture explosive breakdown or reversal points.
    """
    base = marketcap
    return _rolling_kurt(base, 5)

def rvrs_127_kurt_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 97 reverse split signal over 21d to capture explosive breakdown or reversal points.
    """
    base = marketcap
    return _rolling_kurt(base, 21)

def rvrs_128_kurt_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 97 reverse split signal over 63d to capture explosive breakdown or reversal points.
    """
    base = marketcap
    return _rolling_kurt(base, 63)

def rvrs_129_kurt_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 97 reverse split signal over 126d to capture explosive breakdown or reversal points.
    """
    base = marketcap
    return _rolling_kurt(base, 126)

def rvrs_130_kurt_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 97 reverse split signal over 252d to capture explosive breakdown or reversal points.
    """
    base = marketcap
    return _rolling_kurt(base, 252)

def rvrs_131_voladj_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 97 reverse split signal for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap
    return _safe_div(base, _rolling_std(base, 5))

def rvrs_132_voladj_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 97 reverse split signal for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap
    return _safe_div(base, _rolling_std(base, 21))

def rvrs_133_voladj_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 97 reverse split signal for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap
    return _safe_div(base, _rolling_std(base, 63))

def rvrs_134_voladj_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 97 reverse split signal for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap
    return _safe_div(base, _rolling_std(base, 126))

def rvrs_135_voladj_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 97 reverse split signal for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap
    return _safe_div(base, _rolling_std(base, 252))

def rvrs_136_lognorm_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 97 reverse split signal over 5d to stabilize variance and capture exponential shifts.
    """
    base = marketcap
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def rvrs_137_lognorm_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 97 reverse split signal over 21d to stabilize variance and capture exponential shifts.
    """
    base = marketcap
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def rvrs_138_lognorm_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 97 reverse split signal over 63d to stabilize variance and capture exponential shifts.
    """
    base = marketcap
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def rvrs_139_lognorm_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 97 reverse split signal over 126d to stabilize variance and capture exponential shifts.
    """
    base = marketcap
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def rvrs_140_lognorm_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 97 reverse split signal over 252d to stabilize variance and capture exponential shifts.
    """
    base = marketcap
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def rvrs_141_lvl_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 97 reverse split signal over a 5d horizon to identify extreme regimes.
    """
    base = sharesbas
    return _rolling_mean(base, 5)

def rvrs_142_lvl_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 97 reverse split signal over a 21d horizon to identify extreme regimes.
    """
    base = sharesbas
    return _rolling_mean(base, 21)

def rvrs_143_lvl_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 97 reverse split signal over a 63d horizon to identify extreme regimes.
    """
    base = sharesbas
    return _rolling_mean(base, 63)

def rvrs_144_lvl_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 97 reverse split signal over a 126d horizon to identify extreme regimes.
    """
    base = sharesbas
    return _rolling_mean(base, 126)

def rvrs_145_lvl_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 97 reverse split signal over a 252d horizon to identify extreme regimes.
    """
    base = sharesbas
    return _rolling_mean(base, 252)

def rvrs_146_zscore_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 97 reverse split signal by measuring deviations from the 5d mean.
    """
    base = sharesbas
    return _zscore_rolling(base, 5)

def rvrs_147_zscore_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 97 reverse split signal by measuring deviations from the 21d mean.
    """
    base = sharesbas
    return _zscore_rolling(base, 21)

def rvrs_148_zscore_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 97 reverse split signal by measuring deviations from the 63d mean.
    """
    base = sharesbas
    return _zscore_rolling(base, 63)

def rvrs_149_zscore_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 97 reverse split signal by measuring deviations from the 126d mean.
    """
    base = sharesbas
    return _zscore_rolling(base, 126)

def rvrs_150_zscore_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 97 reverse split signal by measuring deviations from the 252d mean.
    """
    base = sharesbas
    return _zscore_rolling(base, 252)
