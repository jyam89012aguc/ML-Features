"""
99_99_going_concern_flags — Base Features 601-675
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

def gcon_601_zscore_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 99 going concern flags by measuring deviations from the 5d mean.
    """
    base = _safe_div(fcf, debt)
    return _zscore_rolling(base, 5)

def gcon_602_zscore_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 99 going concern flags by measuring deviations from the 21d mean.
    """
    base = _safe_div(fcf, debt)
    return _zscore_rolling(base, 21)

def gcon_603_zscore_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 99 going concern flags by measuring deviations from the 63d mean.
    """
    base = _safe_div(fcf, debt)
    return _zscore_rolling(base, 63)

def gcon_604_zscore_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 99 going concern flags by measuring deviations from the 126d mean.
    """
    base = _safe_div(fcf, debt)
    return _zscore_rolling(base, 126)

def gcon_605_zscore_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 99 going concern flags by measuring deviations from the 252d mean.
    """
    base = _safe_div(fcf, debt)
    return _zscore_rolling(base, 252)

def gcon_606_rank_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 99 going concern flags to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = _safe_div(fcf, debt)
    return _rank_pct(base, 5)

def gcon_607_rank_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 99 going concern flags to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = _safe_div(fcf, debt)
    return _rank_pct(base, 21)

def gcon_608_rank_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 99 going concern flags to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = _safe_div(fcf, debt)
    return _rank_pct(base, 63)

def gcon_609_rank_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 99 going concern flags to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = _safe_div(fcf, debt)
    return _rank_pct(base, 126)

def gcon_610_rank_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 99 going concern flags to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = _safe_div(fcf, debt)
    return _rank_pct(base, 252)

def gcon_611_skew_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 99 going concern flags distribution over 5d to detect tail risk or exhaustion.
    """
    base = _safe_div(fcf, debt)
    return _rolling_skew(base, 5)

def gcon_612_skew_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 99 going concern flags distribution over 21d to detect tail risk or exhaustion.
    """
    base = _safe_div(fcf, debt)
    return _rolling_skew(base, 21)

def gcon_613_skew_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 99 going concern flags distribution over 63d to detect tail risk or exhaustion.
    """
    base = _safe_div(fcf, debt)
    return _rolling_skew(base, 63)

def gcon_614_skew_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 99 going concern flags distribution over 126d to detect tail risk or exhaustion.
    """
    base = _safe_div(fcf, debt)
    return _rolling_skew(base, 126)

def gcon_615_skew_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 99 going concern flags distribution over 252d to detect tail risk or exhaustion.
    """
    base = _safe_div(fcf, debt)
    return _rolling_skew(base, 252)

def gcon_616_kurt_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 99 going concern flags over 5d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(fcf, debt)
    return _rolling_kurt(base, 5)

def gcon_617_kurt_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 99 going concern flags over 21d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(fcf, debt)
    return _rolling_kurt(base, 21)

def gcon_618_kurt_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 99 going concern flags over 63d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(fcf, debt)
    return _rolling_kurt(base, 63)

def gcon_619_kurt_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 99 going concern flags over 126d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(fcf, debt)
    return _rolling_kurt(base, 126)

def gcon_620_kurt_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 99 going concern flags over 252d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(fcf, debt)
    return _rolling_kurt(base, 252)

def gcon_621_voladj_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 99 going concern flags for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(fcf, debt)
    return _safe_div(base, _rolling_std(base, 5))

def gcon_622_voladj_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 99 going concern flags for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(fcf, debt)
    return _safe_div(base, _rolling_std(base, 21))

def gcon_623_voladj_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 99 going concern flags for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(fcf, debt)
    return _safe_div(base, _rolling_std(base, 63))

def gcon_624_voladj_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 99 going concern flags for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(fcf, debt)
    return _safe_div(base, _rolling_std(base, 126))

def gcon_625_voladj_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 99 going concern flags for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(fcf, debt)
    return _safe_div(base, _rolling_std(base, 252))

def gcon_626_lognorm_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 99 going concern flags over 5d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(fcf, debt)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def gcon_627_lognorm_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 99 going concern flags over 21d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(fcf, debt)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def gcon_628_lognorm_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 99 going concern flags over 63d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(fcf, debt)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def gcon_629_lognorm_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 99 going concern flags over 126d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(fcf, debt)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def gcon_630_lognorm_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 99 going concern flags over 252d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(fcf, debt)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def gcon_631_lvl_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 99 going concern flags over a 5d horizon to identify extreme regimes.
    """
    base = _safe_div(revenue, sharesbas)
    return _rolling_mean(base, 5)

def gcon_632_lvl_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 99 going concern flags over a 21d horizon to identify extreme regimes.
    """
    base = _safe_div(revenue, sharesbas)
    return _rolling_mean(base, 21)

def gcon_633_lvl_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 99 going concern flags over a 63d horizon to identify extreme regimes.
    """
    base = _safe_div(revenue, sharesbas)
    return _rolling_mean(base, 63)

def gcon_634_lvl_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 99 going concern flags over a 126d horizon to identify extreme regimes.
    """
    base = _safe_div(revenue, sharesbas)
    return _rolling_mean(base, 126)

def gcon_635_lvl_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 99 going concern flags over a 252d horizon to identify extreme regimes.
    """
    base = _safe_div(revenue, sharesbas)
    return _rolling_mean(base, 252)

def gcon_636_zscore_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 99 going concern flags by measuring deviations from the 5d mean.
    """
    base = _safe_div(revenue, sharesbas)
    return _zscore_rolling(base, 5)

def gcon_637_zscore_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 99 going concern flags by measuring deviations from the 21d mean.
    """
    base = _safe_div(revenue, sharesbas)
    return _zscore_rolling(base, 21)

def gcon_638_zscore_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 99 going concern flags by measuring deviations from the 63d mean.
    """
    base = _safe_div(revenue, sharesbas)
    return _zscore_rolling(base, 63)

def gcon_639_zscore_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 99 going concern flags by measuring deviations from the 126d mean.
    """
    base = _safe_div(revenue, sharesbas)
    return _zscore_rolling(base, 126)

def gcon_640_zscore_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 99 going concern flags by measuring deviations from the 252d mean.
    """
    base = _safe_div(revenue, sharesbas)
    return _zscore_rolling(base, 252)

def gcon_641_rank_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 99 going concern flags to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = _safe_div(revenue, sharesbas)
    return _rank_pct(base, 5)

def gcon_642_rank_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 99 going concern flags to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = _safe_div(revenue, sharesbas)
    return _rank_pct(base, 21)

def gcon_643_rank_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 99 going concern flags to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = _safe_div(revenue, sharesbas)
    return _rank_pct(base, 63)

def gcon_644_rank_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 99 going concern flags to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = _safe_div(revenue, sharesbas)
    return _rank_pct(base, 126)

def gcon_645_rank_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 99 going concern flags to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = _safe_div(revenue, sharesbas)
    return _rank_pct(base, 252)

def gcon_646_skew_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 99 going concern flags distribution over 5d to detect tail risk or exhaustion.
    """
    base = _safe_div(revenue, sharesbas)
    return _rolling_skew(base, 5)

def gcon_647_skew_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 99 going concern flags distribution over 21d to detect tail risk or exhaustion.
    """
    base = _safe_div(revenue, sharesbas)
    return _rolling_skew(base, 21)

def gcon_648_skew_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 99 going concern flags distribution over 63d to detect tail risk or exhaustion.
    """
    base = _safe_div(revenue, sharesbas)
    return _rolling_skew(base, 63)

def gcon_649_skew_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 99 going concern flags distribution over 126d to detect tail risk or exhaustion.
    """
    base = _safe_div(revenue, sharesbas)
    return _rolling_skew(base, 126)

def gcon_650_skew_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 99 going concern flags distribution over 252d to detect tail risk or exhaustion.
    """
    base = _safe_div(revenue, sharesbas)
    return _rolling_skew(base, 252)

def gcon_651_kurt_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 99 going concern flags over 5d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(revenue, sharesbas)
    return _rolling_kurt(base, 5)

def gcon_652_kurt_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 99 going concern flags over 21d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(revenue, sharesbas)
    return _rolling_kurt(base, 21)

def gcon_653_kurt_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 99 going concern flags over 63d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(revenue, sharesbas)
    return _rolling_kurt(base, 63)

def gcon_654_kurt_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 99 going concern flags over 126d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(revenue, sharesbas)
    return _rolling_kurt(base, 126)

def gcon_655_kurt_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 99 going concern flags over 252d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(revenue, sharesbas)
    return _rolling_kurt(base, 252)

def gcon_656_voladj_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 99 going concern flags for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(revenue, sharesbas)
    return _safe_div(base, _rolling_std(base, 5))

def gcon_657_voladj_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 99 going concern flags for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(revenue, sharesbas)
    return _safe_div(base, _rolling_std(base, 21))

def gcon_658_voladj_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 99 going concern flags for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(revenue, sharesbas)
    return _safe_div(base, _rolling_std(base, 63))

def gcon_659_voladj_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 99 going concern flags for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(revenue, sharesbas)
    return _safe_div(base, _rolling_std(base, 126))

def gcon_660_voladj_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 99 going concern flags for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(revenue, sharesbas)
    return _safe_div(base, _rolling_std(base, 252))

def gcon_661_lognorm_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 99 going concern flags over 5d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(revenue, sharesbas)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def gcon_662_lognorm_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 99 going concern flags over 21d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(revenue, sharesbas)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def gcon_663_lognorm_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 99 going concern flags over 63d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(revenue, sharesbas)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def gcon_664_lognorm_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 99 going concern flags over 126d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(revenue, sharesbas)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def gcon_665_lognorm_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 99 going concern flags over 252d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(revenue, sharesbas)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def gcon_666_lvl_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 99 going concern flags over a 5d horizon to identify extreme regimes.
    """
    base = _safe_div(liabs, equity)
    return _rolling_mean(base, 5)

def gcon_667_lvl_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 99 going concern flags over a 21d horizon to identify extreme regimes.
    """
    base = _safe_div(liabs, equity)
    return _rolling_mean(base, 21)

def gcon_668_lvl_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 99 going concern flags over a 63d horizon to identify extreme regimes.
    """
    base = _safe_div(liabs, equity)
    return _rolling_mean(base, 63)

def gcon_669_lvl_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 99 going concern flags over a 126d horizon to identify extreme regimes.
    """
    base = _safe_div(liabs, equity)
    return _rolling_mean(base, 126)

def gcon_670_lvl_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 99 going concern flags over a 252d horizon to identify extreme regimes.
    """
    base = _safe_div(liabs, equity)
    return _rolling_mean(base, 252)

def gcon_671_zscore_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 99 going concern flags by measuring deviations from the 5d mean.
    """
    base = _safe_div(liabs, equity)
    return _zscore_rolling(base, 5)

def gcon_672_zscore_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 99 going concern flags by measuring deviations from the 21d mean.
    """
    base = _safe_div(liabs, equity)
    return _zscore_rolling(base, 21)

def gcon_673_zscore_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 99 going concern flags by measuring deviations from the 63d mean.
    """
    base = _safe_div(liabs, equity)
    return _zscore_rolling(base, 63)

def gcon_674_zscore_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 99 going concern flags by measuring deviations from the 126d mean.
    """
    base = _safe_div(liabs, equity)
    return _zscore_rolling(base, 126)

def gcon_675_zscore_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 99 going concern flags by measuring deviations from the 252d mean.
    """
    base = _safe_div(liabs, equity)
    return _zscore_rolling(base, 252)
