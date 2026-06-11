"""
103_103_multi_timeframe_oversold — Base Features 601-675
Domain: 103_multi_timeframe_oversold
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

def mtfo_601_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 103 multi timeframe oversold by measuring deviations from the 5d mean.
    """
    base = _zscore_rolling(close, 175)
    return _zscore_rolling(base, 5)

def mtfo_602_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 103 multi timeframe oversold by measuring deviations from the 21d mean.
    """
    base = _zscore_rolling(close, 175)
    return _zscore_rolling(base, 21)

def mtfo_603_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 103 multi timeframe oversold by measuring deviations from the 63d mean.
    """
    base = _zscore_rolling(close, 175)
    return _zscore_rolling(base, 63)

def mtfo_604_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 103 multi timeframe oversold by measuring deviations from the 126d mean.
    """
    base = _zscore_rolling(close, 175)
    return _zscore_rolling(base, 126)

def mtfo_605_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 103 multi timeframe oversold by measuring deviations from the 252d mean.
    """
    base = _zscore_rolling(close, 175)
    return _zscore_rolling(base, 252)

def mtfo_606_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 103 multi timeframe oversold to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = _zscore_rolling(close, 175)
    return _rank_pct(base, 5)

def mtfo_607_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 103 multi timeframe oversold to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = _zscore_rolling(close, 175)
    return _rank_pct(base, 21)

def mtfo_608_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 103 multi timeframe oversold to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = _zscore_rolling(close, 175)
    return _rank_pct(base, 63)

def mtfo_609_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 103 multi timeframe oversold to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = _zscore_rolling(close, 175)
    return _rank_pct(base, 126)

def mtfo_610_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 103 multi timeframe oversold to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = _zscore_rolling(close, 175)
    return _rank_pct(base, 252)

def mtfo_611_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 103 multi timeframe oversold distribution over 5d to detect tail risk or exhaustion.
    """
    base = _zscore_rolling(close, 175)
    return _rolling_skew(base, 5)

def mtfo_612_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 103 multi timeframe oversold distribution over 21d to detect tail risk or exhaustion.
    """
    base = _zscore_rolling(close, 175)
    return _rolling_skew(base, 21)

def mtfo_613_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 103 multi timeframe oversold distribution over 63d to detect tail risk or exhaustion.
    """
    base = _zscore_rolling(close, 175)
    return _rolling_skew(base, 63)

def mtfo_614_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 103 multi timeframe oversold distribution over 126d to detect tail risk or exhaustion.
    """
    base = _zscore_rolling(close, 175)
    return _rolling_skew(base, 126)

def mtfo_615_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 103 multi timeframe oversold distribution over 252d to detect tail risk or exhaustion.
    """
    base = _zscore_rolling(close, 175)
    return _rolling_skew(base, 252)

def mtfo_616_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 103 multi timeframe oversold over 5d to capture explosive breakdown or reversal points.
    """
    base = _zscore_rolling(close, 175)
    return _rolling_kurt(base, 5)

def mtfo_617_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 103 multi timeframe oversold over 21d to capture explosive breakdown or reversal points.
    """
    base = _zscore_rolling(close, 175)
    return _rolling_kurt(base, 21)

def mtfo_618_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 103 multi timeframe oversold over 63d to capture explosive breakdown or reversal points.
    """
    base = _zscore_rolling(close, 175)
    return _rolling_kurt(base, 63)

def mtfo_619_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 103 multi timeframe oversold over 126d to capture explosive breakdown or reversal points.
    """
    base = _zscore_rolling(close, 175)
    return _rolling_kurt(base, 126)

def mtfo_620_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 103 multi timeframe oversold over 252d to capture explosive breakdown or reversal points.
    """
    base = _zscore_rolling(close, 175)
    return _rolling_kurt(base, 252)

def mtfo_621_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 103 multi timeframe oversold for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = _zscore_rolling(close, 175)
    return _safe_div(base, _rolling_std(base, 5))

def mtfo_622_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 103 multi timeframe oversold for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = _zscore_rolling(close, 175)
    return _safe_div(base, _rolling_std(base, 21))

def mtfo_623_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 103 multi timeframe oversold for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = _zscore_rolling(close, 175)
    return _safe_div(base, _rolling_std(base, 63))

def mtfo_624_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 103 multi timeframe oversold for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = _zscore_rolling(close, 175)
    return _safe_div(base, _rolling_std(base, 126))

def mtfo_625_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 103 multi timeframe oversold for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = _zscore_rolling(close, 175)
    return _safe_div(base, _rolling_std(base, 252))

def mtfo_626_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 103 multi timeframe oversold over 5d to stabilize variance and capture exponential shifts.
    """
    base = _zscore_rolling(close, 175)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def mtfo_627_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 103 multi timeframe oversold over 21d to stabilize variance and capture exponential shifts.
    """
    base = _zscore_rolling(close, 175)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def mtfo_628_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 103 multi timeframe oversold over 63d to stabilize variance and capture exponential shifts.
    """
    base = _zscore_rolling(close, 175)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def mtfo_629_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 103 multi timeframe oversold over 126d to stabilize variance and capture exponential shifts.
    """
    base = _zscore_rolling(close, 175)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def mtfo_630_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 103 multi timeframe oversold over 252d to stabilize variance and capture exponential shifts.
    """
    base = _zscore_rolling(close, 175)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def mtfo_631_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 103 multi timeframe oversold over a 5d horizon to identify extreme regimes.
    """
    base = _zscore_rolling(close, 185)
    return _rolling_mean(base, 5)

def mtfo_632_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 103 multi timeframe oversold over a 21d horizon to identify extreme regimes.
    """
    base = _zscore_rolling(close, 185)
    return _rolling_mean(base, 21)

def mtfo_633_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 103 multi timeframe oversold over a 63d horizon to identify extreme regimes.
    """
    base = _zscore_rolling(close, 185)
    return _rolling_mean(base, 63)

def mtfo_634_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 103 multi timeframe oversold over a 126d horizon to identify extreme regimes.
    """
    base = _zscore_rolling(close, 185)
    return _rolling_mean(base, 126)

def mtfo_635_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 103 multi timeframe oversold over a 252d horizon to identify extreme regimes.
    """
    base = _zscore_rolling(close, 185)
    return _rolling_mean(base, 252)

def mtfo_636_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 103 multi timeframe oversold by measuring deviations from the 5d mean.
    """
    base = _zscore_rolling(close, 185)
    return _zscore_rolling(base, 5)

def mtfo_637_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 103 multi timeframe oversold by measuring deviations from the 21d mean.
    """
    base = _zscore_rolling(close, 185)
    return _zscore_rolling(base, 21)

def mtfo_638_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 103 multi timeframe oversold by measuring deviations from the 63d mean.
    """
    base = _zscore_rolling(close, 185)
    return _zscore_rolling(base, 63)

def mtfo_639_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 103 multi timeframe oversold by measuring deviations from the 126d mean.
    """
    base = _zscore_rolling(close, 185)
    return _zscore_rolling(base, 126)

def mtfo_640_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 103 multi timeframe oversold by measuring deviations from the 252d mean.
    """
    base = _zscore_rolling(close, 185)
    return _zscore_rolling(base, 252)

def mtfo_641_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 103 multi timeframe oversold to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = _zscore_rolling(close, 185)
    return _rank_pct(base, 5)

def mtfo_642_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 103 multi timeframe oversold to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = _zscore_rolling(close, 185)
    return _rank_pct(base, 21)

def mtfo_643_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 103 multi timeframe oversold to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = _zscore_rolling(close, 185)
    return _rank_pct(base, 63)

def mtfo_644_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 103 multi timeframe oversold to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = _zscore_rolling(close, 185)
    return _rank_pct(base, 126)

def mtfo_645_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 103 multi timeframe oversold to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = _zscore_rolling(close, 185)
    return _rank_pct(base, 252)

def mtfo_646_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 103 multi timeframe oversold distribution over 5d to detect tail risk or exhaustion.
    """
    base = _zscore_rolling(close, 185)
    return _rolling_skew(base, 5)

def mtfo_647_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 103 multi timeframe oversold distribution over 21d to detect tail risk or exhaustion.
    """
    base = _zscore_rolling(close, 185)
    return _rolling_skew(base, 21)

def mtfo_648_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 103 multi timeframe oversold distribution over 63d to detect tail risk or exhaustion.
    """
    base = _zscore_rolling(close, 185)
    return _rolling_skew(base, 63)

def mtfo_649_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 103 multi timeframe oversold distribution over 126d to detect tail risk or exhaustion.
    """
    base = _zscore_rolling(close, 185)
    return _rolling_skew(base, 126)

def mtfo_650_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 103 multi timeframe oversold distribution over 252d to detect tail risk or exhaustion.
    """
    base = _zscore_rolling(close, 185)
    return _rolling_skew(base, 252)

def mtfo_651_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 103 multi timeframe oversold over 5d to capture explosive breakdown or reversal points.
    """
    base = _zscore_rolling(close, 185)
    return _rolling_kurt(base, 5)

def mtfo_652_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 103 multi timeframe oversold over 21d to capture explosive breakdown or reversal points.
    """
    base = _zscore_rolling(close, 185)
    return _rolling_kurt(base, 21)

def mtfo_653_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 103 multi timeframe oversold over 63d to capture explosive breakdown or reversal points.
    """
    base = _zscore_rolling(close, 185)
    return _rolling_kurt(base, 63)

def mtfo_654_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 103 multi timeframe oversold over 126d to capture explosive breakdown or reversal points.
    """
    base = _zscore_rolling(close, 185)
    return _rolling_kurt(base, 126)

def mtfo_655_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 103 multi timeframe oversold over 252d to capture explosive breakdown or reversal points.
    """
    base = _zscore_rolling(close, 185)
    return _rolling_kurt(base, 252)

def mtfo_656_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 103 multi timeframe oversold for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = _zscore_rolling(close, 185)
    return _safe_div(base, _rolling_std(base, 5))

def mtfo_657_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 103 multi timeframe oversold for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = _zscore_rolling(close, 185)
    return _safe_div(base, _rolling_std(base, 21))

def mtfo_658_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 103 multi timeframe oversold for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = _zscore_rolling(close, 185)
    return _safe_div(base, _rolling_std(base, 63))

def mtfo_659_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 103 multi timeframe oversold for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = _zscore_rolling(close, 185)
    return _safe_div(base, _rolling_std(base, 126))

def mtfo_660_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 103 multi timeframe oversold for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = _zscore_rolling(close, 185)
    return _safe_div(base, _rolling_std(base, 252))

def mtfo_661_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 103 multi timeframe oversold over 5d to stabilize variance and capture exponential shifts.
    """
    base = _zscore_rolling(close, 185)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def mtfo_662_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 103 multi timeframe oversold over 21d to stabilize variance and capture exponential shifts.
    """
    base = _zscore_rolling(close, 185)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def mtfo_663_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 103 multi timeframe oversold over 63d to stabilize variance and capture exponential shifts.
    """
    base = _zscore_rolling(close, 185)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def mtfo_664_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 103 multi timeframe oversold over 126d to stabilize variance and capture exponential shifts.
    """
    base = _zscore_rolling(close, 185)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def mtfo_665_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 103 multi timeframe oversold over 252d to stabilize variance and capture exponential shifts.
    """
    base = _zscore_rolling(close, 185)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def mtfo_666_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 103 multi timeframe oversold over a 5d horizon to identify extreme regimes.
    """
    base = _zscore_rolling(close, 195)
    return _rolling_mean(base, 5)

def mtfo_667_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 103 multi timeframe oversold over a 21d horizon to identify extreme regimes.
    """
    base = _zscore_rolling(close, 195)
    return _rolling_mean(base, 21)

def mtfo_668_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 103 multi timeframe oversold over a 63d horizon to identify extreme regimes.
    """
    base = _zscore_rolling(close, 195)
    return _rolling_mean(base, 63)

def mtfo_669_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 103 multi timeframe oversold over a 126d horizon to identify extreme regimes.
    """
    base = _zscore_rolling(close, 195)
    return _rolling_mean(base, 126)

def mtfo_670_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 103 multi timeframe oversold over a 252d horizon to identify extreme regimes.
    """
    base = _zscore_rolling(close, 195)
    return _rolling_mean(base, 252)

def mtfo_671_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 103 multi timeframe oversold by measuring deviations from the 5d mean.
    """
    base = _zscore_rolling(close, 195)
    return _zscore_rolling(base, 5)

def mtfo_672_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 103 multi timeframe oversold by measuring deviations from the 21d mean.
    """
    base = _zscore_rolling(close, 195)
    return _zscore_rolling(base, 21)

def mtfo_673_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 103 multi timeframe oversold by measuring deviations from the 63d mean.
    """
    base = _zscore_rolling(close, 195)
    return _zscore_rolling(base, 63)

def mtfo_674_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 103 multi timeframe oversold by measuring deviations from the 126d mean.
    """
    base = _zscore_rolling(close, 195)
    return _zscore_rolling(base, 126)

def mtfo_675_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 103 multi timeframe oversold by measuring deviations from the 252d mean.
    """
    base = _zscore_rolling(close, 195)
    return _zscore_rolling(base, 252)
