"""
114_114_overnight_intraday_split — Base Features 451-525
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

def onid_451_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 114 overnight intraday split over 5d to stabilize variance and capture exponential shifts.
    """
    base = (open / close.shift(13) - 1)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def onid_452_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 114 overnight intraday split over 21d to stabilize variance and capture exponential shifts.
    """
    base = (open / close.shift(13) - 1)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def onid_453_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 114 overnight intraday split over 63d to stabilize variance and capture exponential shifts.
    """
    base = (open / close.shift(13) - 1)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def onid_454_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 114 overnight intraday split over 126d to stabilize variance and capture exponential shifts.
    """
    base = (open / close.shift(13) - 1)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def onid_455_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 114 overnight intraday split over 252d to stabilize variance and capture exponential shifts.
    """
    base = (open / close.shift(13) - 1)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def onid_456_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 114 overnight intraday split over a 5d horizon to identify extreme regimes.
    """
    base = (open / close.shift(14) - 1)
    return _rolling_mean(base, 5)

def onid_457_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 114 overnight intraday split over a 21d horizon to identify extreme regimes.
    """
    base = (open / close.shift(14) - 1)
    return _rolling_mean(base, 21)

def onid_458_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 114 overnight intraday split over a 63d horizon to identify extreme regimes.
    """
    base = (open / close.shift(14) - 1)
    return _rolling_mean(base, 63)

def onid_459_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 114 overnight intraday split over a 126d horizon to identify extreme regimes.
    """
    base = (open / close.shift(14) - 1)
    return _rolling_mean(base, 126)

def onid_460_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 114 overnight intraday split over a 252d horizon to identify extreme regimes.
    """
    base = (open / close.shift(14) - 1)
    return _rolling_mean(base, 252)

def onid_461_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 114 overnight intraday split by measuring deviations from the 5d mean.
    """
    base = (open / close.shift(14) - 1)
    return _zscore_rolling(base, 5)

def onid_462_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 114 overnight intraday split by measuring deviations from the 21d mean.
    """
    base = (open / close.shift(14) - 1)
    return _zscore_rolling(base, 21)

def onid_463_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 114 overnight intraday split by measuring deviations from the 63d mean.
    """
    base = (open / close.shift(14) - 1)
    return _zscore_rolling(base, 63)

def onid_464_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 114 overnight intraday split by measuring deviations from the 126d mean.
    """
    base = (open / close.shift(14) - 1)
    return _zscore_rolling(base, 126)

def onid_465_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 114 overnight intraday split by measuring deviations from the 252d mean.
    """
    base = (open / close.shift(14) - 1)
    return _zscore_rolling(base, 252)

def onid_466_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 114 overnight intraday split to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = (open / close.shift(14) - 1)
    return _rank_pct(base, 5)

def onid_467_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 114 overnight intraday split to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = (open / close.shift(14) - 1)
    return _rank_pct(base, 21)

def onid_468_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 114 overnight intraday split to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = (open / close.shift(14) - 1)
    return _rank_pct(base, 63)

def onid_469_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 114 overnight intraday split to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = (open / close.shift(14) - 1)
    return _rank_pct(base, 126)

def onid_470_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 114 overnight intraday split to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = (open / close.shift(14) - 1)
    return _rank_pct(base, 252)

def onid_471_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 114 overnight intraday split distribution over 5d to detect tail risk or exhaustion.
    """
    base = (open / close.shift(14) - 1)
    return _rolling_skew(base, 5)

def onid_472_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 114 overnight intraday split distribution over 21d to detect tail risk or exhaustion.
    """
    base = (open / close.shift(14) - 1)
    return _rolling_skew(base, 21)

def onid_473_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 114 overnight intraday split distribution over 63d to detect tail risk or exhaustion.
    """
    base = (open / close.shift(14) - 1)
    return _rolling_skew(base, 63)

def onid_474_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 114 overnight intraday split distribution over 126d to detect tail risk or exhaustion.
    """
    base = (open / close.shift(14) - 1)
    return _rolling_skew(base, 126)

def onid_475_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 114 overnight intraday split distribution over 252d to detect tail risk or exhaustion.
    """
    base = (open / close.shift(14) - 1)
    return _rolling_skew(base, 252)

def onid_476_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 114 overnight intraday split over 5d to capture explosive breakdown or reversal points.
    """
    base = (open / close.shift(14) - 1)
    return _rolling_kurt(base, 5)

def onid_477_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 114 overnight intraday split over 21d to capture explosive breakdown or reversal points.
    """
    base = (open / close.shift(14) - 1)
    return _rolling_kurt(base, 21)

def onid_478_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 114 overnight intraday split over 63d to capture explosive breakdown or reversal points.
    """
    base = (open / close.shift(14) - 1)
    return _rolling_kurt(base, 63)

def onid_479_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 114 overnight intraday split over 126d to capture explosive breakdown or reversal points.
    """
    base = (open / close.shift(14) - 1)
    return _rolling_kurt(base, 126)

def onid_480_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 114 overnight intraday split over 252d to capture explosive breakdown or reversal points.
    """
    base = (open / close.shift(14) - 1)
    return _rolling_kurt(base, 252)

def onid_481_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 114 overnight intraday split for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = (open / close.shift(14) - 1)
    return _safe_div(base, _rolling_std(base, 5))

def onid_482_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 114 overnight intraday split for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = (open / close.shift(14) - 1)
    return _safe_div(base, _rolling_std(base, 21))

def onid_483_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 114 overnight intraday split for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = (open / close.shift(14) - 1)
    return _safe_div(base, _rolling_std(base, 63))

def onid_484_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 114 overnight intraday split for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = (open / close.shift(14) - 1)
    return _safe_div(base, _rolling_std(base, 126))

def onid_485_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 114 overnight intraday split for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = (open / close.shift(14) - 1)
    return _safe_div(base, _rolling_std(base, 252))

def onid_486_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 114 overnight intraday split over 5d to stabilize variance and capture exponential shifts.
    """
    base = (open / close.shift(14) - 1)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def onid_487_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 114 overnight intraday split over 21d to stabilize variance and capture exponential shifts.
    """
    base = (open / close.shift(14) - 1)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def onid_488_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 114 overnight intraday split over 63d to stabilize variance and capture exponential shifts.
    """
    base = (open / close.shift(14) - 1)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def onid_489_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 114 overnight intraday split over 126d to stabilize variance and capture exponential shifts.
    """
    base = (open / close.shift(14) - 1)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def onid_490_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 114 overnight intraday split over 252d to stabilize variance and capture exponential shifts.
    """
    base = (open / close.shift(14) - 1)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def onid_491_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 114 overnight intraday split over a 5d horizon to identify extreme regimes.
    """
    base = (open / close.shift(15) - 1)
    return _rolling_mean(base, 5)

def onid_492_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 114 overnight intraday split over a 21d horizon to identify extreme regimes.
    """
    base = (open / close.shift(15) - 1)
    return _rolling_mean(base, 21)

def onid_493_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 114 overnight intraday split over a 63d horizon to identify extreme regimes.
    """
    base = (open / close.shift(15) - 1)
    return _rolling_mean(base, 63)

def onid_494_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 114 overnight intraday split over a 126d horizon to identify extreme regimes.
    """
    base = (open / close.shift(15) - 1)
    return _rolling_mean(base, 126)

def onid_495_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 114 overnight intraday split over a 252d horizon to identify extreme regimes.
    """
    base = (open / close.shift(15) - 1)
    return _rolling_mean(base, 252)

def onid_496_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 114 overnight intraday split by measuring deviations from the 5d mean.
    """
    base = (open / close.shift(15) - 1)
    return _zscore_rolling(base, 5)

def onid_497_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 114 overnight intraday split by measuring deviations from the 21d mean.
    """
    base = (open / close.shift(15) - 1)
    return _zscore_rolling(base, 21)

def onid_498_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 114 overnight intraday split by measuring deviations from the 63d mean.
    """
    base = (open / close.shift(15) - 1)
    return _zscore_rolling(base, 63)

def onid_499_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 114 overnight intraday split by measuring deviations from the 126d mean.
    """
    base = (open / close.shift(15) - 1)
    return _zscore_rolling(base, 126)

def onid_500_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 114 overnight intraday split by measuring deviations from the 252d mean.
    """
    base = (open / close.shift(15) - 1)
    return _zscore_rolling(base, 252)

def onid_501_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 114 overnight intraday split to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = (open / close.shift(15) - 1)
    return _rank_pct(base, 5)

def onid_502_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 114 overnight intraday split to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = (open / close.shift(15) - 1)
    return _rank_pct(base, 21)

def onid_503_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 114 overnight intraday split to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = (open / close.shift(15) - 1)
    return _rank_pct(base, 63)

def onid_504_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 114 overnight intraday split to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = (open / close.shift(15) - 1)
    return _rank_pct(base, 126)

def onid_505_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 114 overnight intraday split to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = (open / close.shift(15) - 1)
    return _rank_pct(base, 252)

def onid_506_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 114 overnight intraday split distribution over 5d to detect tail risk or exhaustion.
    """
    base = (open / close.shift(15) - 1)
    return _rolling_skew(base, 5)

def onid_507_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 114 overnight intraday split distribution over 21d to detect tail risk or exhaustion.
    """
    base = (open / close.shift(15) - 1)
    return _rolling_skew(base, 21)

def onid_508_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 114 overnight intraday split distribution over 63d to detect tail risk or exhaustion.
    """
    base = (open / close.shift(15) - 1)
    return _rolling_skew(base, 63)

def onid_509_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 114 overnight intraday split distribution over 126d to detect tail risk or exhaustion.
    """
    base = (open / close.shift(15) - 1)
    return _rolling_skew(base, 126)

def onid_510_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 114 overnight intraday split distribution over 252d to detect tail risk or exhaustion.
    """
    base = (open / close.shift(15) - 1)
    return _rolling_skew(base, 252)

def onid_511_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 114 overnight intraday split over 5d to capture explosive breakdown or reversal points.
    """
    base = (open / close.shift(15) - 1)
    return _rolling_kurt(base, 5)

def onid_512_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 114 overnight intraday split over 21d to capture explosive breakdown or reversal points.
    """
    base = (open / close.shift(15) - 1)
    return _rolling_kurt(base, 21)

def onid_513_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 114 overnight intraday split over 63d to capture explosive breakdown or reversal points.
    """
    base = (open / close.shift(15) - 1)
    return _rolling_kurt(base, 63)

def onid_514_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 114 overnight intraday split over 126d to capture explosive breakdown or reversal points.
    """
    base = (open / close.shift(15) - 1)
    return _rolling_kurt(base, 126)

def onid_515_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 114 overnight intraday split over 252d to capture explosive breakdown or reversal points.
    """
    base = (open / close.shift(15) - 1)
    return _rolling_kurt(base, 252)

def onid_516_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 114 overnight intraday split for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = (open / close.shift(15) - 1)
    return _safe_div(base, _rolling_std(base, 5))

def onid_517_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 114 overnight intraday split for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = (open / close.shift(15) - 1)
    return _safe_div(base, _rolling_std(base, 21))

def onid_518_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 114 overnight intraday split for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = (open / close.shift(15) - 1)
    return _safe_div(base, _rolling_std(base, 63))

def onid_519_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 114 overnight intraday split for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = (open / close.shift(15) - 1)
    return _safe_div(base, _rolling_std(base, 126))

def onid_520_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 114 overnight intraday split for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = (open / close.shift(15) - 1)
    return _safe_div(base, _rolling_std(base, 252))

def onid_521_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 114 overnight intraday split over 5d to stabilize variance and capture exponential shifts.
    """
    base = (open / close.shift(15) - 1)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def onid_522_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 114 overnight intraday split over 21d to stabilize variance and capture exponential shifts.
    """
    base = (open / close.shift(15) - 1)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def onid_523_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 114 overnight intraday split over 63d to stabilize variance and capture exponential shifts.
    """
    base = (open / close.shift(15) - 1)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def onid_524_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 114 overnight intraday split over 126d to stabilize variance and capture exponential shifts.
    """
    base = (open / close.shift(15) - 1)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def onid_525_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 114 overnight intraday split over 252d to stabilize variance and capture exponential shifts.
    """
    base = (open / close.shift(15) - 1)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))
