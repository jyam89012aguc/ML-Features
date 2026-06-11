"""
114_114_overnight_intraday_split — Base Features 526-600
Domain: 114_overnight_intraday_split
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

def onid_526_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 114 overnight intraday split over a 5d horizon to identify extreme regimes.
    """
    base = (open / close.shift(16) - 1)
    return _rolling_mean(base, 5)

def onid_527_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 114 overnight intraday split over a 21d horizon to identify extreme regimes.
    """
    base = (open / close.shift(16) - 1)
    return _rolling_mean(base, 21)

def onid_528_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 114 overnight intraday split over a 63d horizon to identify extreme regimes.
    """
    base = (open / close.shift(16) - 1)
    return _rolling_mean(base, 63)

def onid_529_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 114 overnight intraday split over a 126d horizon to identify extreme regimes.
    """
    base = (open / close.shift(16) - 1)
    return _rolling_mean(base, 126)

def onid_530_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 114 overnight intraday split over a 252d horizon to identify extreme regimes.
    """
    base = (open / close.shift(16) - 1)
    return _rolling_mean(base, 252)

def onid_531_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 114 overnight intraday split by measuring deviations from the 5d mean.
    """
    base = (open / close.shift(16) - 1)
    return _zscore_rolling(base, 5)

def onid_532_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 114 overnight intraday split by measuring deviations from the 21d mean.
    """
    base = (open / close.shift(16) - 1)
    return _zscore_rolling(base, 21)

def onid_533_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 114 overnight intraday split by measuring deviations from the 63d mean.
    """
    base = (open / close.shift(16) - 1)
    return _zscore_rolling(base, 63)

def onid_534_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 114 overnight intraday split by measuring deviations from the 126d mean.
    """
    base = (open / close.shift(16) - 1)
    return _zscore_rolling(base, 126)

def onid_535_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 114 overnight intraday split by measuring deviations from the 252d mean.
    """
    base = (open / close.shift(16) - 1)
    return _zscore_rolling(base, 252)

def onid_536_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 114 overnight intraday split to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = (open / close.shift(16) - 1)
    return _rank_pct(base, 5)

def onid_537_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 114 overnight intraday split to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = (open / close.shift(16) - 1)
    return _rank_pct(base, 21)

def onid_538_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 114 overnight intraday split to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = (open / close.shift(16) - 1)
    return _rank_pct(base, 63)

def onid_539_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 114 overnight intraday split to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = (open / close.shift(16) - 1)
    return _rank_pct(base, 126)

def onid_540_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 114 overnight intraday split to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = (open / close.shift(16) - 1)
    return _rank_pct(base, 252)

def onid_541_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 114 overnight intraday split distribution over 5d to detect tail risk or exhaustion.
    """
    base = (open / close.shift(16) - 1)
    return _rolling_skew(base, 5)

def onid_542_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 114 overnight intraday split distribution over 21d to detect tail risk or exhaustion.
    """
    base = (open / close.shift(16) - 1)
    return _rolling_skew(base, 21)

def onid_543_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 114 overnight intraday split distribution over 63d to detect tail risk or exhaustion.
    """
    base = (open / close.shift(16) - 1)
    return _rolling_skew(base, 63)

def onid_544_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 114 overnight intraday split distribution over 126d to detect tail risk or exhaustion.
    """
    base = (open / close.shift(16) - 1)
    return _rolling_skew(base, 126)

def onid_545_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 114 overnight intraday split distribution over 252d to detect tail risk or exhaustion.
    """
    base = (open / close.shift(16) - 1)
    return _rolling_skew(base, 252)

def onid_546_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 114 overnight intraday split over 5d to capture explosive breakdown or reversal points.
    """
    base = (open / close.shift(16) - 1)
    return _rolling_kurt(base, 5)

def onid_547_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 114 overnight intraday split over 21d to capture explosive breakdown or reversal points.
    """
    base = (open / close.shift(16) - 1)
    return _rolling_kurt(base, 21)

def onid_548_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 114 overnight intraday split over 63d to capture explosive breakdown or reversal points.
    """
    base = (open / close.shift(16) - 1)
    return _rolling_kurt(base, 63)

def onid_549_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 114 overnight intraday split over 126d to capture explosive breakdown or reversal points.
    """
    base = (open / close.shift(16) - 1)
    return _rolling_kurt(base, 126)

def onid_550_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 114 overnight intraday split over 252d to capture explosive breakdown or reversal points.
    """
    base = (open / close.shift(16) - 1)
    return _rolling_kurt(base, 252)

def onid_551_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 114 overnight intraday split for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = (open / close.shift(16) - 1)
    return _safe_div(base, _rolling_std(base, 5))

def onid_552_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 114 overnight intraday split for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = (open / close.shift(16) - 1)
    return _safe_div(base, _rolling_std(base, 21))

def onid_553_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 114 overnight intraday split for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = (open / close.shift(16) - 1)
    return _safe_div(base, _rolling_std(base, 63))

def onid_554_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 114 overnight intraday split for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = (open / close.shift(16) - 1)
    return _safe_div(base, _rolling_std(base, 126))

def onid_555_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 114 overnight intraday split for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = (open / close.shift(16) - 1)
    return _safe_div(base, _rolling_std(base, 252))

def onid_556_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 114 overnight intraday split over 5d to stabilize variance and capture exponential shifts.
    """
    base = (open / close.shift(16) - 1)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def onid_557_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 114 overnight intraday split over 21d to stabilize variance and capture exponential shifts.
    """
    base = (open / close.shift(16) - 1)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def onid_558_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 114 overnight intraday split over 63d to stabilize variance and capture exponential shifts.
    """
    base = (open / close.shift(16) - 1)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def onid_559_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 114 overnight intraday split over 126d to stabilize variance and capture exponential shifts.
    """
    base = (open / close.shift(16) - 1)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def onid_560_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 114 overnight intraday split over 252d to stabilize variance and capture exponential shifts.
    """
    base = (open / close.shift(16) - 1)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def onid_561_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 114 overnight intraday split over a 5d horizon to identify extreme regimes.
    """
    base = (open / close.shift(17) - 1)
    return _rolling_mean(base, 5)

def onid_562_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 114 overnight intraday split over a 21d horizon to identify extreme regimes.
    """
    base = (open / close.shift(17) - 1)
    return _rolling_mean(base, 21)

def onid_563_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 114 overnight intraday split over a 63d horizon to identify extreme regimes.
    """
    base = (open / close.shift(17) - 1)
    return _rolling_mean(base, 63)

def onid_564_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 114 overnight intraday split over a 126d horizon to identify extreme regimes.
    """
    base = (open / close.shift(17) - 1)
    return _rolling_mean(base, 126)

def onid_565_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 114 overnight intraday split over a 252d horizon to identify extreme regimes.
    """
    base = (open / close.shift(17) - 1)
    return _rolling_mean(base, 252)

def onid_566_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 114 overnight intraday split by measuring deviations from the 5d mean.
    """
    base = (open / close.shift(17) - 1)
    return _zscore_rolling(base, 5)

def onid_567_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 114 overnight intraday split by measuring deviations from the 21d mean.
    """
    base = (open / close.shift(17) - 1)
    return _zscore_rolling(base, 21)

def onid_568_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 114 overnight intraday split by measuring deviations from the 63d mean.
    """
    base = (open / close.shift(17) - 1)
    return _zscore_rolling(base, 63)

def onid_569_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 114 overnight intraday split by measuring deviations from the 126d mean.
    """
    base = (open / close.shift(17) - 1)
    return _zscore_rolling(base, 126)

def onid_570_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 114 overnight intraday split by measuring deviations from the 252d mean.
    """
    base = (open / close.shift(17) - 1)
    return _zscore_rolling(base, 252)

def onid_571_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 114 overnight intraday split to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = (open / close.shift(17) - 1)
    return _rank_pct(base, 5)

def onid_572_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 114 overnight intraday split to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = (open / close.shift(17) - 1)
    return _rank_pct(base, 21)

def onid_573_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 114 overnight intraday split to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = (open / close.shift(17) - 1)
    return _rank_pct(base, 63)

def onid_574_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 114 overnight intraday split to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = (open / close.shift(17) - 1)
    return _rank_pct(base, 126)

def onid_575_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 114 overnight intraday split to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = (open / close.shift(17) - 1)
    return _rank_pct(base, 252)

def onid_576_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 114 overnight intraday split distribution over 5d to detect tail risk or exhaustion.
    """
    base = (open / close.shift(17) - 1)
    return _rolling_skew(base, 5)

def onid_577_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 114 overnight intraday split distribution over 21d to detect tail risk or exhaustion.
    """
    base = (open / close.shift(17) - 1)
    return _rolling_skew(base, 21)

def onid_578_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 114 overnight intraday split distribution over 63d to detect tail risk or exhaustion.
    """
    base = (open / close.shift(17) - 1)
    return _rolling_skew(base, 63)

def onid_579_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 114 overnight intraday split distribution over 126d to detect tail risk or exhaustion.
    """
    base = (open / close.shift(17) - 1)
    return _rolling_skew(base, 126)

def onid_580_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 114 overnight intraday split distribution over 252d to detect tail risk or exhaustion.
    """
    base = (open / close.shift(17) - 1)
    return _rolling_skew(base, 252)

def onid_581_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 114 overnight intraday split over 5d to capture explosive breakdown or reversal points.
    """
    base = (open / close.shift(17) - 1)
    return _rolling_kurt(base, 5)

def onid_582_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 114 overnight intraday split over 21d to capture explosive breakdown or reversal points.
    """
    base = (open / close.shift(17) - 1)
    return _rolling_kurt(base, 21)

def onid_583_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 114 overnight intraday split over 63d to capture explosive breakdown or reversal points.
    """
    base = (open / close.shift(17) - 1)
    return _rolling_kurt(base, 63)

def onid_584_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 114 overnight intraday split over 126d to capture explosive breakdown or reversal points.
    """
    base = (open / close.shift(17) - 1)
    return _rolling_kurt(base, 126)

def onid_585_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 114 overnight intraday split over 252d to capture explosive breakdown or reversal points.
    """
    base = (open / close.shift(17) - 1)
    return _rolling_kurt(base, 252)

def onid_586_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 114 overnight intraday split for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = (open / close.shift(17) - 1)
    return _safe_div(base, _rolling_std(base, 5))

def onid_587_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 114 overnight intraday split for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = (open / close.shift(17) - 1)
    return _safe_div(base, _rolling_std(base, 21))

def onid_588_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 114 overnight intraday split for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = (open / close.shift(17) - 1)
    return _safe_div(base, _rolling_std(base, 63))

def onid_589_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 114 overnight intraday split for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = (open / close.shift(17) - 1)
    return _safe_div(base, _rolling_std(base, 126))

def onid_590_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 114 overnight intraday split for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = (open / close.shift(17) - 1)
    return _safe_div(base, _rolling_std(base, 252))

def onid_591_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 114 overnight intraday split over 5d to stabilize variance and capture exponential shifts.
    """
    base = (open / close.shift(17) - 1)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def onid_592_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 114 overnight intraday split over 21d to stabilize variance and capture exponential shifts.
    """
    base = (open / close.shift(17) - 1)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def onid_593_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 114 overnight intraday split over 63d to stabilize variance and capture exponential shifts.
    """
    base = (open / close.shift(17) - 1)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def onid_594_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 114 overnight intraday split over 126d to stabilize variance and capture exponential shifts.
    """
    base = (open / close.shift(17) - 1)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def onid_595_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 114 overnight intraday split over 252d to stabilize variance and capture exponential shifts.
    """
    base = (open / close.shift(17) - 1)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def onid_596_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 114 overnight intraday split over a 5d horizon to identify extreme regimes.
    """
    base = (open / close.shift(18) - 1)
    return _rolling_mean(base, 5)

def onid_597_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 114 overnight intraday split over a 21d horizon to identify extreme regimes.
    """
    base = (open / close.shift(18) - 1)
    return _rolling_mean(base, 21)

def onid_598_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 114 overnight intraday split over a 63d horizon to identify extreme regimes.
    """
    base = (open / close.shift(18) - 1)
    return _rolling_mean(base, 63)

def onid_599_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 114 overnight intraday split over a 126d horizon to identify extreme regimes.
    """
    base = (open / close.shift(18) - 1)
    return _rolling_mean(base, 126)

def onid_600_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 114 overnight intraday split over a 252d horizon to identify extreme regimes.
    """
    base = (open / close.shift(18) - 1)
    return _rolling_mean(base, 252)
