"""
97_97_reverse_split_signal — Base Features 601-675
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

def rvrs_601_zscore_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 97 reverse split signal by measuring deviations from the 5d mean.
    """
    base = _safe_div(fcf, debt)
    return _zscore_rolling(base, 5)

def rvrs_602_zscore_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 97 reverse split signal by measuring deviations from the 21d mean.
    """
    base = _safe_div(fcf, debt)
    return _zscore_rolling(base, 21)

def rvrs_603_zscore_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 97 reverse split signal by measuring deviations from the 63d mean.
    """
    base = _safe_div(fcf, debt)
    return _zscore_rolling(base, 63)

def rvrs_604_zscore_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 97 reverse split signal by measuring deviations from the 126d mean.
    """
    base = _safe_div(fcf, debt)
    return _zscore_rolling(base, 126)

def rvrs_605_zscore_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 97 reverse split signal by measuring deviations from the 252d mean.
    """
    base = _safe_div(fcf, debt)
    return _zscore_rolling(base, 252)

def rvrs_606_rank_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 97 reverse split signal to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = _safe_div(fcf, debt)
    return _rank_pct(base, 5)

def rvrs_607_rank_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 97 reverse split signal to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = _safe_div(fcf, debt)
    return _rank_pct(base, 21)

def rvrs_608_rank_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 97 reverse split signal to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = _safe_div(fcf, debt)
    return _rank_pct(base, 63)

def rvrs_609_rank_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 97 reverse split signal to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = _safe_div(fcf, debt)
    return _rank_pct(base, 126)

def rvrs_610_rank_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 97 reverse split signal to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = _safe_div(fcf, debt)
    return _rank_pct(base, 252)

def rvrs_611_skew_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 97 reverse split signal distribution over 5d to detect tail risk or exhaustion.
    """
    base = _safe_div(fcf, debt)
    return _rolling_skew(base, 5)

def rvrs_612_skew_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 97 reverse split signal distribution over 21d to detect tail risk or exhaustion.
    """
    base = _safe_div(fcf, debt)
    return _rolling_skew(base, 21)

def rvrs_613_skew_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 97 reverse split signal distribution over 63d to detect tail risk or exhaustion.
    """
    base = _safe_div(fcf, debt)
    return _rolling_skew(base, 63)

def rvrs_614_skew_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 97 reverse split signal distribution over 126d to detect tail risk or exhaustion.
    """
    base = _safe_div(fcf, debt)
    return _rolling_skew(base, 126)

def rvrs_615_skew_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 97 reverse split signal distribution over 252d to detect tail risk or exhaustion.
    """
    base = _safe_div(fcf, debt)
    return _rolling_skew(base, 252)

def rvrs_616_kurt_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 97 reverse split signal over 5d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(fcf, debt)
    return _rolling_kurt(base, 5)

def rvrs_617_kurt_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 97 reverse split signal over 21d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(fcf, debt)
    return _rolling_kurt(base, 21)

def rvrs_618_kurt_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 97 reverse split signal over 63d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(fcf, debt)
    return _rolling_kurt(base, 63)

def rvrs_619_kurt_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 97 reverse split signal over 126d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(fcf, debt)
    return _rolling_kurt(base, 126)

def rvrs_620_kurt_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 97 reverse split signal over 252d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(fcf, debt)
    return _rolling_kurt(base, 252)

def rvrs_621_voladj_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 97 reverse split signal for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(fcf, debt)
    return _safe_div(base, _rolling_std(base, 5))

def rvrs_622_voladj_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 97 reverse split signal for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(fcf, debt)
    return _safe_div(base, _rolling_std(base, 21))

def rvrs_623_voladj_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 97 reverse split signal for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(fcf, debt)
    return _safe_div(base, _rolling_std(base, 63))

def rvrs_624_voladj_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 97 reverse split signal for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(fcf, debt)
    return _safe_div(base, _rolling_std(base, 126))

def rvrs_625_voladj_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 97 reverse split signal for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(fcf, debt)
    return _safe_div(base, _rolling_std(base, 252))

def rvrs_626_lognorm_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 97 reverse split signal over 5d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(fcf, debt)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def rvrs_627_lognorm_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 97 reverse split signal over 21d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(fcf, debt)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def rvrs_628_lognorm_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 97 reverse split signal over 63d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(fcf, debt)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def rvrs_629_lognorm_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 97 reverse split signal over 126d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(fcf, debt)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def rvrs_630_lognorm_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 97 reverse split signal over 252d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(fcf, debt)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def rvrs_631_lvl_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 97 reverse split signal over a 5d horizon to identify extreme regimes.
    """
    base = _safe_div(revenue, sharesbas)
    return _rolling_mean(base, 5)

def rvrs_632_lvl_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 97 reverse split signal over a 21d horizon to identify extreme regimes.
    """
    base = _safe_div(revenue, sharesbas)
    return _rolling_mean(base, 21)

def rvrs_633_lvl_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 97 reverse split signal over a 63d horizon to identify extreme regimes.
    """
    base = _safe_div(revenue, sharesbas)
    return _rolling_mean(base, 63)

def rvrs_634_lvl_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 97 reverse split signal over a 126d horizon to identify extreme regimes.
    """
    base = _safe_div(revenue, sharesbas)
    return _rolling_mean(base, 126)

def rvrs_635_lvl_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 97 reverse split signal over a 252d horizon to identify extreme regimes.
    """
    base = _safe_div(revenue, sharesbas)
    return _rolling_mean(base, 252)

def rvrs_636_zscore_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 97 reverse split signal by measuring deviations from the 5d mean.
    """
    base = _safe_div(revenue, sharesbas)
    return _zscore_rolling(base, 5)

def rvrs_637_zscore_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 97 reverse split signal by measuring deviations from the 21d mean.
    """
    base = _safe_div(revenue, sharesbas)
    return _zscore_rolling(base, 21)

def rvrs_638_zscore_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 97 reverse split signal by measuring deviations from the 63d mean.
    """
    base = _safe_div(revenue, sharesbas)
    return _zscore_rolling(base, 63)

def rvrs_639_zscore_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 97 reverse split signal by measuring deviations from the 126d mean.
    """
    base = _safe_div(revenue, sharesbas)
    return _zscore_rolling(base, 126)

def rvrs_640_zscore_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 97 reverse split signal by measuring deviations from the 252d mean.
    """
    base = _safe_div(revenue, sharesbas)
    return _zscore_rolling(base, 252)

def rvrs_641_rank_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 97 reverse split signal to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = _safe_div(revenue, sharesbas)
    return _rank_pct(base, 5)

def rvrs_642_rank_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 97 reverse split signal to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = _safe_div(revenue, sharesbas)
    return _rank_pct(base, 21)

def rvrs_643_rank_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 97 reverse split signal to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = _safe_div(revenue, sharesbas)
    return _rank_pct(base, 63)

def rvrs_644_rank_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 97 reverse split signal to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = _safe_div(revenue, sharesbas)
    return _rank_pct(base, 126)

def rvrs_645_rank_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 97 reverse split signal to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = _safe_div(revenue, sharesbas)
    return _rank_pct(base, 252)

def rvrs_646_skew_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 97 reverse split signal distribution over 5d to detect tail risk or exhaustion.
    """
    base = _safe_div(revenue, sharesbas)
    return _rolling_skew(base, 5)

def rvrs_647_skew_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 97 reverse split signal distribution over 21d to detect tail risk or exhaustion.
    """
    base = _safe_div(revenue, sharesbas)
    return _rolling_skew(base, 21)

def rvrs_648_skew_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 97 reverse split signal distribution over 63d to detect tail risk or exhaustion.
    """
    base = _safe_div(revenue, sharesbas)
    return _rolling_skew(base, 63)

def rvrs_649_skew_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 97 reverse split signal distribution over 126d to detect tail risk or exhaustion.
    """
    base = _safe_div(revenue, sharesbas)
    return _rolling_skew(base, 126)

def rvrs_650_skew_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 97 reverse split signal distribution over 252d to detect tail risk or exhaustion.
    """
    base = _safe_div(revenue, sharesbas)
    return _rolling_skew(base, 252)

def rvrs_651_kurt_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 97 reverse split signal over 5d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(revenue, sharesbas)
    return _rolling_kurt(base, 5)

def rvrs_652_kurt_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 97 reverse split signal over 21d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(revenue, sharesbas)
    return _rolling_kurt(base, 21)

def rvrs_653_kurt_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 97 reverse split signal over 63d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(revenue, sharesbas)
    return _rolling_kurt(base, 63)

def rvrs_654_kurt_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 97 reverse split signal over 126d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(revenue, sharesbas)
    return _rolling_kurt(base, 126)

def rvrs_655_kurt_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 97 reverse split signal over 252d to capture explosive breakdown or reversal points.
    """
    base = _safe_div(revenue, sharesbas)
    return _rolling_kurt(base, 252)

def rvrs_656_voladj_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 97 reverse split signal for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(revenue, sharesbas)
    return _safe_div(base, _rolling_std(base, 5))

def rvrs_657_voladj_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 97 reverse split signal for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(revenue, sharesbas)
    return _safe_div(base, _rolling_std(base, 21))

def rvrs_658_voladj_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 97 reverse split signal for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(revenue, sharesbas)
    return _safe_div(base, _rolling_std(base, 63))

def rvrs_659_voladj_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 97 reverse split signal for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(revenue, sharesbas)
    return _safe_div(base, _rolling_std(base, 126))

def rvrs_660_voladj_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 97 reverse split signal for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = _safe_div(revenue, sharesbas)
    return _safe_div(base, _rolling_std(base, 252))

def rvrs_661_lognorm_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 97 reverse split signal over 5d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(revenue, sharesbas)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def rvrs_662_lognorm_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 97 reverse split signal over 21d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(revenue, sharesbas)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def rvrs_663_lognorm_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 97 reverse split signal over 63d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(revenue, sharesbas)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def rvrs_664_lognorm_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 97 reverse split signal over 126d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(revenue, sharesbas)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def rvrs_665_lognorm_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 97 reverse split signal over 252d to stabilize variance and capture exponential shifts.
    """
    base = _safe_div(revenue, sharesbas)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def rvrs_666_lvl_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 97 reverse split signal over a 5d horizon to identify extreme regimes.
    """
    base = _safe_div(liabs, equity)
    return _rolling_mean(base, 5)

def rvrs_667_lvl_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 97 reverse split signal over a 21d horizon to identify extreme regimes.
    """
    base = _safe_div(liabs, equity)
    return _rolling_mean(base, 21)

def rvrs_668_lvl_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 97 reverse split signal over a 63d horizon to identify extreme regimes.
    """
    base = _safe_div(liabs, equity)
    return _rolling_mean(base, 63)

def rvrs_669_lvl_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 97 reverse split signal over a 126d horizon to identify extreme regimes.
    """
    base = _safe_div(liabs, equity)
    return _rolling_mean(base, 126)

def rvrs_670_lvl_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 97 reverse split signal over a 252d horizon to identify extreme regimes.
    """
    base = _safe_div(liabs, equity)
    return _rolling_mean(base, 252)

def rvrs_671_zscore_5d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 97 reverse split signal by measuring deviations from the 5d mean.
    """
    base = _safe_div(liabs, equity)
    return _zscore_rolling(base, 5)

def rvrs_672_zscore_21d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 97 reverse split signal by measuring deviations from the 21d mean.
    """
    base = _safe_div(liabs, equity)
    return _zscore_rolling(base, 21)

def rvrs_673_zscore_63d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 97 reverse split signal by measuring deviations from the 63d mean.
    """
    base = _safe_div(liabs, equity)
    return _zscore_rolling(base, 63)

def rvrs_674_zscore_126d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 97 reverse split signal by measuring deviations from the 126d mean.
    """
    base = _safe_div(liabs, equity)
    return _zscore_rolling(base, 126)

def rvrs_675_zscore_252d(revenue: pd.Series, netinc: pd.Series, ocf: pd.Series, fcf: pd.Series, sharesbas: pd.Series, assets: pd.Series, liabs: pd.Series, equity: pd.Series, debt: pd.Series, ps: pd.Series, pb: pd.Series, marketcap: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 97 reverse split signal by measuring deviations from the 252d mean.
    """
    base = _safe_div(liabs, equity)
    return _zscore_rolling(base, 252)
