"""
60_60_earnings_collapse — Base Features 601-675
Domain: 60_earnings_collapse
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

def ecol_601_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 60 earnings collapse by measuring deviations from the 5d mean.
    """
    base = (close.pct_change(18).rolling(90).mean())
    return _zscore_rolling(base, 5)

def ecol_602_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 60 earnings collapse by measuring deviations from the 21d mean.
    """
    base = (close.pct_change(18).rolling(90).mean())
    return _zscore_rolling(base, 21)

def ecol_603_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 60 earnings collapse by measuring deviations from the 63d mean.
    """
    base = (close.pct_change(18).rolling(90).mean())
    return _zscore_rolling(base, 63)

def ecol_604_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 60 earnings collapse by measuring deviations from the 126d mean.
    """
    base = (close.pct_change(18).rolling(90).mean())
    return _zscore_rolling(base, 126)

def ecol_605_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 60 earnings collapse by measuring deviations from the 252d mean.
    """
    base = (close.pct_change(18).rolling(90).mean())
    return _zscore_rolling(base, 252)

def ecol_606_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 60 earnings collapse to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = (close.pct_change(18).rolling(90).mean())
    return _rank_pct(base, 5)

def ecol_607_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 60 earnings collapse to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = (close.pct_change(18).rolling(90).mean())
    return _rank_pct(base, 21)

def ecol_608_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 60 earnings collapse to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = (close.pct_change(18).rolling(90).mean())
    return _rank_pct(base, 63)

def ecol_609_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 60 earnings collapse to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = (close.pct_change(18).rolling(90).mean())
    return _rank_pct(base, 126)

def ecol_610_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 60 earnings collapse to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = (close.pct_change(18).rolling(90).mean())
    return _rank_pct(base, 252)

def ecol_611_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 60 earnings collapse distribution over 5d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(18).rolling(90).mean())
    return _rolling_skew(base, 5)

def ecol_612_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 60 earnings collapse distribution over 21d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(18).rolling(90).mean())
    return _rolling_skew(base, 21)

def ecol_613_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 60 earnings collapse distribution over 63d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(18).rolling(90).mean())
    return _rolling_skew(base, 63)

def ecol_614_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 60 earnings collapse distribution over 126d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(18).rolling(90).mean())
    return _rolling_skew(base, 126)

def ecol_615_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 60 earnings collapse distribution over 252d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(18).rolling(90).mean())
    return _rolling_skew(base, 252)

def ecol_616_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 60 earnings collapse over 5d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(18).rolling(90).mean())
    return _rolling_kurt(base, 5)

def ecol_617_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 60 earnings collapse over 21d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(18).rolling(90).mean())
    return _rolling_kurt(base, 21)

def ecol_618_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 60 earnings collapse over 63d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(18).rolling(90).mean())
    return _rolling_kurt(base, 63)

def ecol_619_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 60 earnings collapse over 126d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(18).rolling(90).mean())
    return _rolling_kurt(base, 126)

def ecol_620_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 60 earnings collapse over 252d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(18).rolling(90).mean())
    return _rolling_kurt(base, 252)

def ecol_621_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 60 earnings collapse for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(18).rolling(90).mean())
    return _safe_div(base, _rolling_std(base, 5))

def ecol_622_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 60 earnings collapse for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(18).rolling(90).mean())
    return _safe_div(base, _rolling_std(base, 21))

def ecol_623_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 60 earnings collapse for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(18).rolling(90).mean())
    return _safe_div(base, _rolling_std(base, 63))

def ecol_624_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 60 earnings collapse for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(18).rolling(90).mean())
    return _safe_div(base, _rolling_std(base, 126))

def ecol_625_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 60 earnings collapse for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(18).rolling(90).mean())
    return _safe_div(base, _rolling_std(base, 252))

def ecol_626_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 60 earnings collapse over 5d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(18).rolling(90).mean())
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def ecol_627_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 60 earnings collapse over 21d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(18).rolling(90).mean())
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def ecol_628_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 60 earnings collapse over 63d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(18).rolling(90).mean())
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def ecol_629_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 60 earnings collapse over 126d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(18).rolling(90).mean())
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def ecol_630_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 60 earnings collapse over 252d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(18).rolling(90).mean())
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def ecol_631_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 60 earnings collapse over a 5d horizon to identify extreme regimes.
    """
    base = (close.pct_change(19).rolling(95).mean())
    return _rolling_mean(base, 5)

def ecol_632_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 60 earnings collapse over a 21d horizon to identify extreme regimes.
    """
    base = (close.pct_change(19).rolling(95).mean())
    return _rolling_mean(base, 21)

def ecol_633_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 60 earnings collapse over a 63d horizon to identify extreme regimes.
    """
    base = (close.pct_change(19).rolling(95).mean())
    return _rolling_mean(base, 63)

def ecol_634_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 60 earnings collapse over a 126d horizon to identify extreme regimes.
    """
    base = (close.pct_change(19).rolling(95).mean())
    return _rolling_mean(base, 126)

def ecol_635_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 60 earnings collapse over a 252d horizon to identify extreme regimes.
    """
    base = (close.pct_change(19).rolling(95).mean())
    return _rolling_mean(base, 252)

def ecol_636_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 60 earnings collapse by measuring deviations from the 5d mean.
    """
    base = (close.pct_change(19).rolling(95).mean())
    return _zscore_rolling(base, 5)

def ecol_637_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 60 earnings collapse by measuring deviations from the 21d mean.
    """
    base = (close.pct_change(19).rolling(95).mean())
    return _zscore_rolling(base, 21)

def ecol_638_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 60 earnings collapse by measuring deviations from the 63d mean.
    """
    base = (close.pct_change(19).rolling(95).mean())
    return _zscore_rolling(base, 63)

def ecol_639_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 60 earnings collapse by measuring deviations from the 126d mean.
    """
    base = (close.pct_change(19).rolling(95).mean())
    return _zscore_rolling(base, 126)

def ecol_640_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 60 earnings collapse by measuring deviations from the 252d mean.
    """
    base = (close.pct_change(19).rolling(95).mean())
    return _zscore_rolling(base, 252)

def ecol_641_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 60 earnings collapse to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = (close.pct_change(19).rolling(95).mean())
    return _rank_pct(base, 5)

def ecol_642_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 60 earnings collapse to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = (close.pct_change(19).rolling(95).mean())
    return _rank_pct(base, 21)

def ecol_643_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 60 earnings collapse to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = (close.pct_change(19).rolling(95).mean())
    return _rank_pct(base, 63)

def ecol_644_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 60 earnings collapse to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = (close.pct_change(19).rolling(95).mean())
    return _rank_pct(base, 126)

def ecol_645_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 60 earnings collapse to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = (close.pct_change(19).rolling(95).mean())
    return _rank_pct(base, 252)

def ecol_646_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 60 earnings collapse distribution over 5d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(19).rolling(95).mean())
    return _rolling_skew(base, 5)

def ecol_647_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 60 earnings collapse distribution over 21d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(19).rolling(95).mean())
    return _rolling_skew(base, 21)

def ecol_648_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 60 earnings collapse distribution over 63d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(19).rolling(95).mean())
    return _rolling_skew(base, 63)

def ecol_649_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 60 earnings collapse distribution over 126d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(19).rolling(95).mean())
    return _rolling_skew(base, 126)

def ecol_650_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 60 earnings collapse distribution over 252d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(19).rolling(95).mean())
    return _rolling_skew(base, 252)

def ecol_651_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 60 earnings collapse over 5d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(19).rolling(95).mean())
    return _rolling_kurt(base, 5)

def ecol_652_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 60 earnings collapse over 21d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(19).rolling(95).mean())
    return _rolling_kurt(base, 21)

def ecol_653_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 60 earnings collapse over 63d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(19).rolling(95).mean())
    return _rolling_kurt(base, 63)

def ecol_654_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 60 earnings collapse over 126d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(19).rolling(95).mean())
    return _rolling_kurt(base, 126)

def ecol_655_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 60 earnings collapse over 252d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(19).rolling(95).mean())
    return _rolling_kurt(base, 252)

def ecol_656_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 60 earnings collapse for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(19).rolling(95).mean())
    return _safe_div(base, _rolling_std(base, 5))

def ecol_657_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 60 earnings collapse for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(19).rolling(95).mean())
    return _safe_div(base, _rolling_std(base, 21))

def ecol_658_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 60 earnings collapse for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(19).rolling(95).mean())
    return _safe_div(base, _rolling_std(base, 63))

def ecol_659_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 60 earnings collapse for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(19).rolling(95).mean())
    return _safe_div(base, _rolling_std(base, 126))

def ecol_660_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 60 earnings collapse for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(19).rolling(95).mean())
    return _safe_div(base, _rolling_std(base, 252))

def ecol_661_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 60 earnings collapse over 5d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(19).rolling(95).mean())
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def ecol_662_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 60 earnings collapse over 21d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(19).rolling(95).mean())
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def ecol_663_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 60 earnings collapse over 63d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(19).rolling(95).mean())
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def ecol_664_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 60 earnings collapse over 126d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(19).rolling(95).mean())
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def ecol_665_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 60 earnings collapse over 252d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(19).rolling(95).mean())
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def ecol_666_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 60 earnings collapse over a 5d horizon to identify extreme regimes.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return _rolling_mean(base, 5)

def ecol_667_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 60 earnings collapse over a 21d horizon to identify extreme regimes.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return _rolling_mean(base, 21)

def ecol_668_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 60 earnings collapse over a 63d horizon to identify extreme regimes.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return _rolling_mean(base, 63)

def ecol_669_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 60 earnings collapse over a 126d horizon to identify extreme regimes.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return _rolling_mean(base, 126)

def ecol_670_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 60 earnings collapse over a 252d horizon to identify extreme regimes.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return _rolling_mean(base, 252)

def ecol_671_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 60 earnings collapse by measuring deviations from the 5d mean.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return _zscore_rolling(base, 5)

def ecol_672_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 60 earnings collapse by measuring deviations from the 21d mean.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return _zscore_rolling(base, 21)

def ecol_673_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 60 earnings collapse by measuring deviations from the 63d mean.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return _zscore_rolling(base, 63)

def ecol_674_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 60 earnings collapse by measuring deviations from the 126d mean.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return _zscore_rolling(base, 126)

def ecol_675_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 60 earnings collapse by measuring deviations from the 252d mean.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return _zscore_rolling(base, 252)
