"""
99_99_going_concern_flags — Base Features 676-750
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

def gcon_676_rank_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 99 going concern flags to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = _safe_div(liabs, equity)
    return _rank_pct(base, 5)

def gcon_677_rank_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 99 going concern flags to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = _safe_div(liabs, equity)
    return _rank_pct(base, 21)

def gcon_678_rank_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 99 going concern flags to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = _safe_div(liabs, equity)
    return _rank_pct(base, 63)

def gcon_679_rank_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 99 going concern flags to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = _safe_div(liabs, equity)
    return _rank_pct(base, 126)

def gcon_680_rank_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 99 going concern flags to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = _safe_div(liabs, equity)
    return _rank_pct(base, 252)

def gcon_681_skew_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 99 going concern flags distribution over 5d to detect tail risk or exhaustion.
    """
    base = _safe_div(liabs, equity)
    return _rolling_skew(base, 5)

def gcon_682_skew_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 99 going concern flags distribution over 21d to detect tail risk or exhaustion.
    """
    base = _safe_div(liabs, equity)
    return _rolling_skew(base, 21)

def gcon_683_skew_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 99 going concern flags distribution over 63d to detect tail risk or exhaustion.
    """
    base = _safe_div(liabs, equity)
    return _rolling_skew(base, 63)

def gcon_684_skew_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 99 going concern flags distribution over 126d to detect tail risk or exhaustion.
    """
    base = _safe_div(liabs, equity)
    return _rolling_skew(base, 126)

def gcon_685_skew_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 99 going concern flags distribution over 252d to detect tail risk or exhaustion.
    """
    base = _safe_div(liabs, equity)
    return _rolling_skew(base, 252)

def gcon_686_kurt_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 99 going concern flags over 5d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(liabs, equity)
    return _rolling_kurt(base, 5)

def gcon_687_kurt_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 99 going concern flags over 21d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(liabs, equity)
    return _rolling_kurt(base, 21)

def gcon_688_kurt_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 99 going concern flags over 63d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(liabs, equity)
    return _rolling_kurt(base, 63)

def gcon_689_kurt_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 99 going concern flags over 126d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(liabs, equity)
    return _rolling_kurt(base, 126)

def gcon_690_kurt_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 99 going concern flags over 252d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(liabs, equity)
    return _rolling_kurt(base, 252)

def gcon_691_voladj_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 99 going concern flags for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(liabs, equity)
    return _safe_div(base, _rolling_std(base, 5))

def gcon_692_voladj_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 99 going concern flags for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(liabs, equity)
    return _safe_div(base, _rolling_std(base, 21))

def gcon_693_voladj_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 99 going concern flags for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(liabs, equity)
    return _safe_div(base, _rolling_std(base, 63))

def gcon_694_voladj_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 99 going concern flags for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(liabs, equity)
    return _safe_div(base, _rolling_std(base, 126))

def gcon_695_voladj_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 99 going concern flags for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(liabs, equity)
    return _safe_div(base, _rolling_std(base, 252))

def gcon_696_lognorm_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 99 going concern flags over 5d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(liabs, equity)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def gcon_697_lognorm_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 99 going concern flags over 21d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(liabs, equity)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def gcon_698_lognorm_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 99 going concern flags over 63d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(liabs, equity)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def gcon_699_lognorm_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 99 going concern flags over 126d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(liabs, equity)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def gcon_700_lognorm_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 99 going concern flags over 252d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(liabs, equity)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def gcon_701_lvl_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 99 going concern flags over a 5d horizon to identify extreme regimes.
    """
    base = _safe_div(ocf, debt)
    return _rolling_mean(base, 5)

def gcon_702_lvl_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 99 going concern flags over a 21d horizon to identify extreme regimes.
    """
    base = _safe_div(ocf, debt)
    return _rolling_mean(base, 21)

def gcon_703_lvl_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 99 going concern flags over a 63d horizon to identify extreme regimes.
    """
    base = _safe_div(ocf, debt)
    return _rolling_mean(base, 63)

def gcon_704_lvl_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 99 going concern flags over a 126d horizon to identify extreme regimes.
    """
    base = _safe_div(ocf, debt)
    return _rolling_mean(base, 126)

def gcon_705_lvl_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 99 going concern flags over a 252d horizon to identify extreme regimes.
    """
    base = _safe_div(ocf, debt)
    return _rolling_mean(base, 252)

def gcon_706_zscore_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 99 going concern flags by measuring deviations from the 5d mean.
    """
    base = _safe_div(ocf, debt)
    return _zscore_rolling(base, 5)

def gcon_707_zscore_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 99 going concern flags by measuring deviations from the 21d mean.
    """
    base = _safe_div(ocf, debt)
    return _zscore_rolling(base, 21)

def gcon_708_zscore_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 99 going concern flags by measuring deviations from the 63d mean.
    """
    base = _safe_div(ocf, debt)
    return _zscore_rolling(base, 63)

def gcon_709_zscore_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 99 going concern flags by measuring deviations from the 126d mean.
    """
    base = _safe_div(ocf, debt)
    return _zscore_rolling(base, 126)

def gcon_710_zscore_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 99 going concern flags by measuring deviations from the 252d mean.
    """
    base = _safe_div(ocf, debt)
    return _zscore_rolling(base, 252)

def gcon_711_rank_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 99 going concern flags to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = _safe_div(ocf, debt)
    return _rank_pct(base, 5)

def gcon_712_rank_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 99 going concern flags to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = _safe_div(ocf, debt)
    return _rank_pct(base, 21)

def gcon_713_rank_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 99 going concern flags to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = _safe_div(ocf, debt)
    return _rank_pct(base, 63)

def gcon_714_rank_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 99 going concern flags to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = _safe_div(ocf, debt)
    return _rank_pct(base, 126)

def gcon_715_rank_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 99 going concern flags to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = _safe_div(ocf, debt)
    return _rank_pct(base, 252)

def gcon_716_skew_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 99 going concern flags distribution over 5d to detect tail risk or exhaustion.
    """
    base = _safe_div(ocf, debt)
    return _rolling_skew(base, 5)

def gcon_717_skew_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 99 going concern flags distribution over 21d to detect tail risk or exhaustion.
    """
    base = _safe_div(ocf, debt)
    return _rolling_skew(base, 21)

def gcon_718_skew_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 99 going concern flags distribution over 63d to detect tail risk or exhaustion.
    """
    base = _safe_div(ocf, debt)
    return _rolling_skew(base, 63)

def gcon_719_skew_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 99 going concern flags distribution over 126d to detect tail risk or exhaustion.
    """
    base = _safe_div(ocf, debt)
    return _rolling_skew(base, 126)

def gcon_720_skew_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 99 going concern flags distribution over 252d to detect tail risk or exhaustion.
    """
    base = _safe_div(ocf, debt)
    return _rolling_skew(base, 252)

def gcon_721_kurt_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 99 going concern flags over 5d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(ocf, debt)
    return _rolling_kurt(base, 5)

def gcon_722_kurt_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 99 going concern flags over 21d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(ocf, debt)
    return _rolling_kurt(base, 21)

def gcon_723_kurt_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 99 going concern flags over 63d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(ocf, debt)
    return _rolling_kurt(base, 63)

def gcon_724_kurt_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 99 going concern flags over 126d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(ocf, debt)
    return _rolling_kurt(base, 126)

def gcon_725_kurt_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 99 going concern flags over 252d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(ocf, debt)
    return _rolling_kurt(base, 252)

def gcon_726_voladj_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 99 going concern flags for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(ocf, debt)
    return _safe_div(base, _rolling_std(base, 5))

def gcon_727_voladj_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 99 going concern flags for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(ocf, debt)
    return _safe_div(base, _rolling_std(base, 21))

def gcon_728_voladj_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 99 going concern flags for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(ocf, debt)
    return _safe_div(base, _rolling_std(base, 63))

def gcon_729_voladj_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 99 going concern flags for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(ocf, debt)
    return _safe_div(base, _rolling_std(base, 126))

def gcon_730_voladj_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 99 going concern flags for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(ocf, debt)
    return _safe_div(base, _rolling_std(base, 252))

def gcon_731_lognorm_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 99 going concern flags over 5d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(ocf, debt)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def gcon_732_lognorm_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 99 going concern flags over 21d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(ocf, debt)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def gcon_733_lognorm_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 99 going concern flags over 63d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(ocf, debt)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def gcon_734_lognorm_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 99 going concern flags over 126d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(ocf, debt)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def gcon_735_lognorm_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 99 going concern flags over 252d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(ocf, debt)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def gcon_736_lvl_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 99 going concern flags over a 5d horizon to identify extreme regimes.
    """
    base = _safe_div(netinc, equity)
    return _rolling_mean(base, 5)

def gcon_737_lvl_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 99 going concern flags over a 21d horizon to identify extreme regimes.
    """
    base = _safe_div(netinc, equity)
    return _rolling_mean(base, 21)

def gcon_738_lvl_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 99 going concern flags over a 63d horizon to identify extreme regimes.
    """
    base = _safe_div(netinc, equity)
    return _rolling_mean(base, 63)

def gcon_739_lvl_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 99 going concern flags over a 126d horizon to identify extreme regimes.
    """
    base = _safe_div(netinc, equity)
    return _rolling_mean(base, 126)

def gcon_740_lvl_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 99 going concern flags over a 252d horizon to identify extreme regimes.
    """
    base = _safe_div(netinc, equity)
    return _rolling_mean(base, 252)

def gcon_741_zscore_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 99 going concern flags by measuring deviations from the 5d mean.
    """
    base = _safe_div(netinc, equity)
    return _zscore_rolling(base, 5)

def gcon_742_zscore_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 99 going concern flags by measuring deviations from the 21d mean.
    """
    base = _safe_div(netinc, equity)
    return _zscore_rolling(base, 21)

def gcon_743_zscore_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 99 going concern flags by measuring deviations from the 63d mean.
    """
    base = _safe_div(netinc, equity)
    return _zscore_rolling(base, 63)

def gcon_744_zscore_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 99 going concern flags by measuring deviations from the 126d mean.
    """
    base = _safe_div(netinc, equity)
    return _zscore_rolling(base, 126)

def gcon_745_zscore_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 99 going concern flags by measuring deviations from the 252d mean.
    """
    base = _safe_div(netinc, equity)
    return _zscore_rolling(base, 252)

def gcon_746_rank_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 99 going concern flags to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = _safe_div(netinc, equity)
    return _rank_pct(base, 5)

def gcon_747_rank_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 99 going concern flags to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = _safe_div(netinc, equity)
    return _rank_pct(base, 21)

def gcon_748_rank_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 99 going concern flags to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = _safe_div(netinc, equity)
    return _rank_pct(base, 63)

def gcon_749_rank_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 99 going concern flags to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = _safe_div(netinc, equity)
    return _rank_pct(base, 126)

def gcon_750_rank_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 99 going concern flags to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = _safe_div(netinc, equity)
    return _rank_pct(base, 252)
