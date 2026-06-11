"""
40_40_close_location — Base Features 601-675
Domain: 40_close_location
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

def cloc_601_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 40 close location by measuring deviations from the 5d mean.
    """
    base = (close.pct_change(18).rolling(90).mean())
    return _zscore_rolling(base, 5)

def cloc_602_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 40 close location by measuring deviations from the 21d mean.
    """
    base = (close.pct_change(18).rolling(90).mean())
    return _zscore_rolling(base, 21)

def cloc_603_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 40 close location by measuring deviations from the 63d mean.
    """
    base = (close.pct_change(18).rolling(90).mean())
    return _zscore_rolling(base, 63)

def cloc_604_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 40 close location by measuring deviations from the 126d mean.
    """
    base = (close.pct_change(18).rolling(90).mean())
    return _zscore_rolling(base, 126)

def cloc_605_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 40 close location by measuring deviations from the 252d mean.
    """
    base = (close.pct_change(18).rolling(90).mean())
    return _zscore_rolling(base, 252)

def cloc_606_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 40 close location to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = (close.pct_change(18).rolling(90).mean())
    return _rank_pct(base, 5)

def cloc_607_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 40 close location to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = (close.pct_change(18).rolling(90).mean())
    return _rank_pct(base, 21)

def cloc_608_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 40 close location to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = (close.pct_change(18).rolling(90).mean())
    return _rank_pct(base, 63)

def cloc_609_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 40 close location to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = (close.pct_change(18).rolling(90).mean())
    return _rank_pct(base, 126)

def cloc_610_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 40 close location to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = (close.pct_change(18).rolling(90).mean())
    return _rank_pct(base, 252)

def cloc_611_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 40 close location distribution over 5d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(18).rolling(90).mean())
    return _rolling_skew(base, 5)

def cloc_612_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 40 close location distribution over 21d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(18).rolling(90).mean())
    return _rolling_skew(base, 21)

def cloc_613_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 40 close location distribution over 63d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(18).rolling(90).mean())
    return _rolling_skew(base, 63)

def cloc_614_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 40 close location distribution over 126d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(18).rolling(90).mean())
    return _rolling_skew(base, 126)

def cloc_615_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 40 close location distribution over 252d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(18).rolling(90).mean())
    return _rolling_skew(base, 252)

def cloc_616_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 40 close location over 5d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(18).rolling(90).mean())
    return _rolling_kurt(base, 5)

def cloc_617_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 40 close location over 21d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(18).rolling(90).mean())
    return _rolling_kurt(base, 21)

def cloc_618_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 40 close location over 63d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(18).rolling(90).mean())
    return _rolling_kurt(base, 63)

def cloc_619_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 40 close location over 126d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(18).rolling(90).mean())
    return _rolling_kurt(base, 126)

def cloc_620_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 40 close location over 252d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(18).rolling(90).mean())
    return _rolling_kurt(base, 252)

def cloc_621_voladj_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 40 close location for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(18).rolling(90).mean())
    return _safe_div(base, _rolling_std(base, 5))

def cloc_622_voladj_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 40 close location for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(18).rolling(90).mean())
    return _safe_div(base, _rolling_std(base, 21))

def cloc_623_voladj_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 40 close location for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(18).rolling(90).mean())
    return _safe_div(base, _rolling_std(base, 63))

def cloc_624_voladj_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 40 close location for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(18).rolling(90).mean())
    return _safe_div(base, _rolling_std(base, 126))

def cloc_625_voladj_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 40 close location for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(18).rolling(90).mean())
    return _safe_div(base, _rolling_std(base, 252))

def cloc_626_lognorm_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 40 close location over 5d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(18).rolling(90).mean())
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def cloc_627_lognorm_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 40 close location over 21d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(18).rolling(90).mean())
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def cloc_628_lognorm_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 40 close location over 63d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(18).rolling(90).mean())
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def cloc_629_lognorm_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 40 close location over 126d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(18).rolling(90).mean())
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def cloc_630_lognorm_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 40 close location over 252d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(18).rolling(90).mean())
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def cloc_631_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 40 close location over a 5d horizon to identify extreme regimes.
    """
    base = (close.pct_change(19).rolling(95).mean())
    return _rolling_mean(base, 5)

def cloc_632_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 40 close location over a 21d horizon to identify extreme regimes.
    """
    base = (close.pct_change(19).rolling(95).mean())
    return _rolling_mean(base, 21)

def cloc_633_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 40 close location over a 63d horizon to identify extreme regimes.
    """
    base = (close.pct_change(19).rolling(95).mean())
    return _rolling_mean(base, 63)

def cloc_634_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 40 close location over a 126d horizon to identify extreme regimes.
    """
    base = (close.pct_change(19).rolling(95).mean())
    return _rolling_mean(base, 126)

def cloc_635_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 40 close location over a 252d horizon to identify extreme regimes.
    """
    base = (close.pct_change(19).rolling(95).mean())
    return _rolling_mean(base, 252)

def cloc_636_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 40 close location by measuring deviations from the 5d mean.
    """
    base = (close.pct_change(19).rolling(95).mean())
    return _zscore_rolling(base, 5)

def cloc_637_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 40 close location by measuring deviations from the 21d mean.
    """
    base = (close.pct_change(19).rolling(95).mean())
    return _zscore_rolling(base, 21)

def cloc_638_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 40 close location by measuring deviations from the 63d mean.
    """
    base = (close.pct_change(19).rolling(95).mean())
    return _zscore_rolling(base, 63)

def cloc_639_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 40 close location by measuring deviations from the 126d mean.
    """
    base = (close.pct_change(19).rolling(95).mean())
    return _zscore_rolling(base, 126)

def cloc_640_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 40 close location by measuring deviations from the 252d mean.
    """
    base = (close.pct_change(19).rolling(95).mean())
    return _zscore_rolling(base, 252)

def cloc_641_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 40 close location to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = (close.pct_change(19).rolling(95).mean())
    return _rank_pct(base, 5)

def cloc_642_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 40 close location to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = (close.pct_change(19).rolling(95).mean())
    return _rank_pct(base, 21)

def cloc_643_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 40 close location to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = (close.pct_change(19).rolling(95).mean())
    return _rank_pct(base, 63)

def cloc_644_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 40 close location to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = (close.pct_change(19).rolling(95).mean())
    return _rank_pct(base, 126)

def cloc_645_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 40 close location to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = (close.pct_change(19).rolling(95).mean())
    return _rank_pct(base, 252)

def cloc_646_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 40 close location distribution over 5d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(19).rolling(95).mean())
    return _rolling_skew(base, 5)

def cloc_647_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 40 close location distribution over 21d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(19).rolling(95).mean())
    return _rolling_skew(base, 21)

def cloc_648_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 40 close location distribution over 63d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(19).rolling(95).mean())
    return _rolling_skew(base, 63)

def cloc_649_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 40 close location distribution over 126d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(19).rolling(95).mean())
    return _rolling_skew(base, 126)

def cloc_650_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 40 close location distribution over 252d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(19).rolling(95).mean())
    return _rolling_skew(base, 252)

def cloc_651_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 40 close location over 5d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(19).rolling(95).mean())
    return _rolling_kurt(base, 5)

def cloc_652_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 40 close location over 21d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(19).rolling(95).mean())
    return _rolling_kurt(base, 21)

def cloc_653_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 40 close location over 63d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(19).rolling(95).mean())
    return _rolling_kurt(base, 63)

def cloc_654_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 40 close location over 126d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(19).rolling(95).mean())
    return _rolling_kurt(base, 126)

def cloc_655_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 40 close location over 252d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(19).rolling(95).mean())
    return _rolling_kurt(base, 252)

def cloc_656_voladj_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 40 close location for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(19).rolling(95).mean())
    return _safe_div(base, _rolling_std(base, 5))

def cloc_657_voladj_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 40 close location for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(19).rolling(95).mean())
    return _safe_div(base, _rolling_std(base, 21))

def cloc_658_voladj_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 40 close location for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(19).rolling(95).mean())
    return _safe_div(base, _rolling_std(base, 63))

def cloc_659_voladj_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 40 close location for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(19).rolling(95).mean())
    return _safe_div(base, _rolling_std(base, 126))

def cloc_660_voladj_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 40 close location for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(19).rolling(95).mean())
    return _safe_div(base, _rolling_std(base, 252))

def cloc_661_lognorm_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 40 close location over 5d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(19).rolling(95).mean())
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def cloc_662_lognorm_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 40 close location over 21d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(19).rolling(95).mean())
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def cloc_663_lognorm_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 40 close location over 63d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(19).rolling(95).mean())
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def cloc_664_lognorm_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 40 close location over 126d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(19).rolling(95).mean())
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def cloc_665_lognorm_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 40 close location over 252d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(19).rolling(95).mean())
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def cloc_666_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 40 close location over a 5d horizon to identify extreme regimes.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return _rolling_mean(base, 5)

def cloc_667_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 40 close location over a 21d horizon to identify extreme regimes.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return _rolling_mean(base, 21)

def cloc_668_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 40 close location over a 63d horizon to identify extreme regimes.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return _rolling_mean(base, 63)

def cloc_669_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 40 close location over a 126d horizon to identify extreme regimes.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return _rolling_mean(base, 126)

def cloc_670_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 40 close location over a 252d horizon to identify extreme regimes.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return _rolling_mean(base, 252)

def cloc_671_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 40 close location by measuring deviations from the 5d mean.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return _zscore_rolling(base, 5)

def cloc_672_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 40 close location by measuring deviations from the 21d mean.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return _zscore_rolling(base, 21)

def cloc_673_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 40 close location by measuring deviations from the 63d mean.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return _zscore_rolling(base, 63)

def cloc_674_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 40 close location by measuring deviations from the 126d mean.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return _zscore_rolling(base, 126)

def cloc_675_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 40 close location by measuring deviations from the 252d mean.
    """
    base = (close.pct_change(20).rolling(100).mean())
    return _zscore_rolling(base, 252)
