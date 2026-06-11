"""
99_99_going_concern_flags — Base Features 076-150
Domain: 99_going_concern_flags
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

def gcon_076_zscore_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 99 going concern flags by measuring deviations from the 5d mean.
    """
    base = _safe_div(assets - liabs, assets)
    return _zscore_rolling(base, 5)

def gcon_077_zscore_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 99 going concern flags by measuring deviations from the 21d mean.
    """
    base = _safe_div(assets - liabs, assets)
    return _zscore_rolling(base, 21)

def gcon_078_zscore_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 99 going concern flags by measuring deviations from the 63d mean.
    """
    base = _safe_div(assets - liabs, assets)
    return _zscore_rolling(base, 63)

def gcon_079_zscore_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 99 going concern flags by measuring deviations from the 126d mean.
    """
    base = _safe_div(assets - liabs, assets)
    return _zscore_rolling(base, 126)

def gcon_080_zscore_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 99 going concern flags by measuring deviations from the 252d mean.
    """
    base = _safe_div(assets - liabs, assets)
    return _zscore_rolling(base, 252)

def gcon_081_rank_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 99 going concern flags to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = _safe_div(assets - liabs, assets)
    return _rank_pct(base, 5)

def gcon_082_rank_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 99 going concern flags to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = _safe_div(assets - liabs, assets)
    return _rank_pct(base, 21)

def gcon_083_rank_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 99 going concern flags to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = _safe_div(assets - liabs, assets)
    return _rank_pct(base, 63)

def gcon_084_rank_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 99 going concern flags to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = _safe_div(assets - liabs, assets)
    return _rank_pct(base, 126)

def gcon_085_rank_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 99 going concern flags to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = _safe_div(assets - liabs, assets)
    return _rank_pct(base, 252)

def gcon_086_skew_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 99 going concern flags distribution over 5d to detect tail risk or exhaustion.
    """
    base = _safe_div(assets - liabs, assets)
    return _rolling_skew(base, 5)

def gcon_087_skew_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 99 going concern flags distribution over 21d to detect tail risk or exhaustion.
    """
    base = _safe_div(assets - liabs, assets)
    return _rolling_skew(base, 21)

def gcon_088_skew_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 99 going concern flags distribution over 63d to detect tail risk or exhaustion.
    """
    base = _safe_div(assets - liabs, assets)
    return _rolling_skew(base, 63)

def gcon_089_skew_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 99 going concern flags distribution over 126d to detect tail risk or exhaustion.
    """
    base = _safe_div(assets - liabs, assets)
    return _rolling_skew(base, 126)

def gcon_090_skew_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 99 going concern flags distribution over 252d to detect tail risk or exhaustion.
    """
    base = _safe_div(assets - liabs, assets)
    return _rolling_skew(base, 252)

def gcon_091_kurt_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 99 going concern flags over 5d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(assets - liabs, assets)
    return _rolling_kurt(base, 5)

def gcon_092_kurt_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 99 going concern flags over 21d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(assets - liabs, assets)
    return _rolling_kurt(base, 21)

def gcon_093_kurt_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 99 going concern flags over 63d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(assets - liabs, assets)
    return _rolling_kurt(base, 63)

def gcon_094_kurt_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 99 going concern flags over 126d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(assets - liabs, assets)
    return _rolling_kurt(base, 126)

def gcon_095_kurt_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 99 going concern flags over 252d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(assets - liabs, assets)
    return _rolling_kurt(base, 252)

def gcon_096_voladj_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 99 going concern flags for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(assets - liabs, assets)
    return _safe_div(base, _rolling_std(base, 5))

def gcon_097_voladj_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 99 going concern flags for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(assets - liabs, assets)
    return _safe_div(base, _rolling_std(base, 21))

def gcon_098_voladj_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 99 going concern flags for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(assets - liabs, assets)
    return _safe_div(base, _rolling_std(base, 63))

def gcon_099_voladj_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 99 going concern flags for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(assets - liabs, assets)
    return _safe_div(base, _rolling_std(base, 126))

def gcon_100_voladj_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 99 going concern flags for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(assets - liabs, assets)
    return _safe_div(base, _rolling_std(base, 252))

def gcon_101_lognorm_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 99 going concern flags over 5d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(assets - liabs, assets)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def gcon_102_lognorm_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 99 going concern flags over 21d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(assets - liabs, assets)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def gcon_103_lognorm_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 99 going concern flags over 63d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(assets - liabs, assets)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def gcon_104_lognorm_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 99 going concern flags over 126d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(assets - liabs, assets)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def gcon_105_lognorm_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 99 going concern flags over 252d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(assets - liabs, assets)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def gcon_106_lvl_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 99 going concern flags over a 5d horizon to identify extreme regimes.
    """
    base = marketcap
    return _rolling_mean(base, 5)

def gcon_107_lvl_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 99 going concern flags over a 21d horizon to identify extreme regimes.
    """
    base = marketcap
    return _rolling_mean(base, 21)

def gcon_108_lvl_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 99 going concern flags over a 63d horizon to identify extreme regimes.
    """
    base = marketcap
    return _rolling_mean(base, 63)

def gcon_109_lvl_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 99 going concern flags over a 126d horizon to identify extreme regimes.
    """
    base = marketcap
    return _rolling_mean(base, 126)

def gcon_110_lvl_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 99 going concern flags over a 252d horizon to identify extreme regimes.
    """
    base = marketcap
    return _rolling_mean(base, 252)

def gcon_111_zscore_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 99 going concern flags by measuring deviations from the 5d mean.
    """
    base = marketcap
    return _zscore_rolling(base, 5)

def gcon_112_zscore_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 99 going concern flags by measuring deviations from the 21d mean.
    """
    base = marketcap
    return _zscore_rolling(base, 21)

def gcon_113_zscore_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 99 going concern flags by measuring deviations from the 63d mean.
    """
    base = marketcap
    return _zscore_rolling(base, 63)

def gcon_114_zscore_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 99 going concern flags by measuring deviations from the 126d mean.
    """
    base = marketcap
    return _zscore_rolling(base, 126)

def gcon_115_zscore_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 99 going concern flags by measuring deviations from the 252d mean.
    """
    base = marketcap
    return _zscore_rolling(base, 252)

def gcon_116_rank_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 99 going concern flags to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = marketcap
    return _rank_pct(base, 5)

def gcon_117_rank_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 99 going concern flags to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = marketcap
    return _rank_pct(base, 21)

def gcon_118_rank_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 99 going concern flags to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = marketcap
    return _rank_pct(base, 63)

def gcon_119_rank_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 99 going concern flags to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = marketcap
    return _rank_pct(base, 126)

def gcon_120_rank_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 99 going concern flags to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = marketcap
    return _rank_pct(base, 252)

def gcon_121_skew_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 99 going concern flags distribution over 5d to detect tail risk or exhaustion.
    """
    base = marketcap
    return _rolling_skew(base, 5)

def gcon_122_skew_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 99 going concern flags distribution over 21d to detect tail risk or exhaustion.
    """
    base = marketcap
    return _rolling_skew(base, 21)

def gcon_123_skew_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 99 going concern flags distribution over 63d to detect tail risk or exhaustion.
    """
    base = marketcap
    return _rolling_skew(base, 63)

def gcon_124_skew_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 99 going concern flags distribution over 126d to detect tail risk or exhaustion.
    """
    base = marketcap
    return _rolling_skew(base, 126)

def gcon_125_skew_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 99 going concern flags distribution over 252d to detect tail risk or exhaustion.
    """
    base = marketcap
    return _rolling_skew(base, 252)

def gcon_126_kurt_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 99 going concern flags over 5d to capture explosive breakdown or reversal points.
    """
    base = marketcap
    return _rolling_kurt(base, 5)

def gcon_127_kurt_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 99 going concern flags over 21d to capture explosive breakdown or reversal points.
    """
    base = marketcap
    return _rolling_kurt(base, 21)

def gcon_128_kurt_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 99 going concern flags over 63d to capture explosive breakdown or reversal points.
    """
    base = marketcap
    return _rolling_kurt(base, 63)

def gcon_129_kurt_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 99 going concern flags over 126d to capture explosive breakdown or reversal points.
    """
    base = marketcap
    return _rolling_kurt(base, 126)

def gcon_130_kurt_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 99 going concern flags over 252d to capture explosive breakdown or reversal points.
    """
    base = marketcap
    return _rolling_kurt(base, 252)

def gcon_131_voladj_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 99 going concern flags for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap
    return _safe_div(base, _rolling_std(base, 5))

def gcon_132_voladj_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 99 going concern flags for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap
    return _safe_div(base, _rolling_std(base, 21))

def gcon_133_voladj_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 99 going concern flags for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap
    return _safe_div(base, _rolling_std(base, 63))

def gcon_134_voladj_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 99 going concern flags for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap
    return _safe_div(base, _rolling_std(base, 126))

def gcon_135_voladj_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 99 going concern flags for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = marketcap
    return _safe_div(base, _rolling_std(base, 252))

def gcon_136_lognorm_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 99 going concern flags over 5d to stabilize variance and capture exponential shifts.
    """
    base = marketcap
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def gcon_137_lognorm_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 99 going concern flags over 21d to stabilize variance and capture exponential shifts.
    """
    base = marketcap
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def gcon_138_lognorm_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 99 going concern flags over 63d to stabilize variance and capture exponential shifts.
    """
    base = marketcap
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def gcon_139_lognorm_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 99 going concern flags over 126d to stabilize variance and capture exponential shifts.
    """
    base = marketcap
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def gcon_140_lognorm_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 99 going concern flags over 252d to stabilize variance and capture exponential shifts.
    """
    base = marketcap
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def gcon_141_lvl_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 99 going concern flags over a 5d horizon to identify extreme regimes.
    """
    base = sharesbas
    return _rolling_mean(base, 5)

def gcon_142_lvl_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 99 going concern flags over a 21d horizon to identify extreme regimes.
    """
    base = sharesbas
    return _rolling_mean(base, 21)

def gcon_143_lvl_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 99 going concern flags over a 63d horizon to identify extreme regimes.
    """
    base = sharesbas
    return _rolling_mean(base, 63)

def gcon_144_lvl_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 99 going concern flags over a 126d horizon to identify extreme regimes.
    """
    base = sharesbas
    return _rolling_mean(base, 126)

def gcon_145_lvl_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 99 going concern flags over a 252d horizon to identify extreme regimes.
    """
    base = sharesbas
    return _rolling_mean(base, 252)

def gcon_146_zscore_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 99 going concern flags by measuring deviations from the 5d mean.
    """
    base = sharesbas
    return _zscore_rolling(base, 5)

def gcon_147_zscore_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 99 going concern flags by measuring deviations from the 21d mean.
    """
    base = sharesbas
    return _zscore_rolling(base, 21)

def gcon_148_zscore_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 99 going concern flags by measuring deviations from the 63d mean.
    """
    base = sharesbas
    return _zscore_rolling(base, 63)

def gcon_149_zscore_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 99 going concern flags by measuring deviations from the 126d mean.
    """
    base = sharesbas
    return _zscore_rolling(base, 126)

def gcon_150_zscore_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 99 going concern flags by measuring deviations from the 252d mean.
    """
    base = sharesbas
    return _zscore_rolling(base, 252)
