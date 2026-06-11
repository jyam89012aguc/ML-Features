"""
112_112_volume_at_price — Base Features 451-525
Domain: 112_volume_at_price
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

def vapr_451_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 112 volume at price over 5d to stabilize variance and capture exponential shifts.
    """
    base = volume * close.pct_change(13)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def vapr_452_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 112 volume at price over 21d to stabilize variance and capture exponential shifts.
    """
    base = volume * close.pct_change(13)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def vapr_453_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 112 volume at price over 63d to stabilize variance and capture exponential shifts.
    """
    base = volume * close.pct_change(13)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def vapr_454_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 112 volume at price over 126d to stabilize variance and capture exponential shifts.
    """
    base = volume * close.pct_change(13)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def vapr_455_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 112 volume at price over 252d to stabilize variance and capture exponential shifts.
    """
    base = volume * close.pct_change(13)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def vapr_456_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 112 volume at price over a 5d horizon to identify extreme regimes.
    """
    base = volume * close.pct_change(14)
    return _rolling_mean(base, 5)

def vapr_457_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 112 volume at price over a 21d horizon to identify extreme regimes.
    """
    base = volume * close.pct_change(14)
    return _rolling_mean(base, 21)

def vapr_458_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 112 volume at price over a 63d horizon to identify extreme regimes.
    """
    base = volume * close.pct_change(14)
    return _rolling_mean(base, 63)

def vapr_459_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 112 volume at price over a 126d horizon to identify extreme regimes.
    """
    base = volume * close.pct_change(14)
    return _rolling_mean(base, 126)

def vapr_460_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 112 volume at price over a 252d horizon to identify extreme regimes.
    """
    base = volume * close.pct_change(14)
    return _rolling_mean(base, 252)

def vapr_461_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 112 volume at price by measuring deviations from the 5d mean.
    """
    base = volume * close.pct_change(14)
    return _zscore_rolling(base, 5)

def vapr_462_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 112 volume at price by measuring deviations from the 21d mean.
    """
    base = volume * close.pct_change(14)
    return _zscore_rolling(base, 21)

def vapr_463_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 112 volume at price by measuring deviations from the 63d mean.
    """
    base = volume * close.pct_change(14)
    return _zscore_rolling(base, 63)

def vapr_464_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 112 volume at price by measuring deviations from the 126d mean.
    """
    base = volume * close.pct_change(14)
    return _zscore_rolling(base, 126)

def vapr_465_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 112 volume at price by measuring deviations from the 252d mean.
    """
    base = volume * close.pct_change(14)
    return _zscore_rolling(base, 252)

def vapr_466_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 112 volume at price to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = volume * close.pct_change(14)
    return _rank_pct(base, 5)

def vapr_467_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 112 volume at price to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = volume * close.pct_change(14)
    return _rank_pct(base, 21)

def vapr_468_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 112 volume at price to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = volume * close.pct_change(14)
    return _rank_pct(base, 63)

def vapr_469_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 112 volume at price to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = volume * close.pct_change(14)
    return _rank_pct(base, 126)

def vapr_470_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 112 volume at price to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = volume * close.pct_change(14)
    return _rank_pct(base, 252)

def vapr_471_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 112 volume at price distribution over 5d to detect tail risk or exhaustion.
    """
    base = volume * close.pct_change(14)
    return _rolling_skew(base, 5)

def vapr_472_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 112 volume at price distribution over 21d to detect tail risk or exhaustion.
    """
    base = volume * close.pct_change(14)
    return _rolling_skew(base, 21)

def vapr_473_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 112 volume at price distribution over 63d to detect tail risk or exhaustion.
    """
    base = volume * close.pct_change(14)
    return _rolling_skew(base, 63)

def vapr_474_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 112 volume at price distribution over 126d to detect tail risk or exhaustion.
    """
    base = volume * close.pct_change(14)
    return _rolling_skew(base, 126)

def vapr_475_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 112 volume at price distribution over 252d to detect tail risk or exhaustion.
    """
    base = volume * close.pct_change(14)
    return _rolling_skew(base, 252)

def vapr_476_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 112 volume at price over 5d to capture explosive breakdown or reversal points.
    """
    base = volume * close.pct_change(14)
    return _rolling_kurt(base, 5)

def vapr_477_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 112 volume at price over 21d to capture explosive breakdown or reversal points.
    """
    base = volume * close.pct_change(14)
    return _rolling_kurt(base, 21)

def vapr_478_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 112 volume at price over 63d to capture explosive breakdown or reversal points.
    """
    base = volume * close.pct_change(14)
    return _rolling_kurt(base, 63)

def vapr_479_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 112 volume at price over 126d to capture explosive breakdown or reversal points.
    """
    base = volume * close.pct_change(14)
    return _rolling_kurt(base, 126)

def vapr_480_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 112 volume at price over 252d to capture explosive breakdown or reversal points.
    """
    base = volume * close.pct_change(14)
    return _rolling_kurt(base, 252)

def vapr_481_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 112 volume at price for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = volume * close.pct_change(14)
    return _safe_div(base, _rolling_std(base, 5))

def vapr_482_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 112 volume at price for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = volume * close.pct_change(14)
    return _safe_div(base, _rolling_std(base, 21))

def vapr_483_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 112 volume at price for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = volume * close.pct_change(14)
    return _safe_div(base, _rolling_std(base, 63))

def vapr_484_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 112 volume at price for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = volume * close.pct_change(14)
    return _safe_div(base, _rolling_std(base, 126))

def vapr_485_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 112 volume at price for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = volume * close.pct_change(14)
    return _safe_div(base, _rolling_std(base, 252))

def vapr_486_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 112 volume at price over 5d to stabilize variance and capture exponential shifts.
    """
    base = volume * close.pct_change(14)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def vapr_487_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 112 volume at price over 21d to stabilize variance and capture exponential shifts.
    """
    base = volume * close.pct_change(14)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def vapr_488_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 112 volume at price over 63d to stabilize variance and capture exponential shifts.
    """
    base = volume * close.pct_change(14)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def vapr_489_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 112 volume at price over 126d to stabilize variance and capture exponential shifts.
    """
    base = volume * close.pct_change(14)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def vapr_490_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 112 volume at price over 252d to stabilize variance and capture exponential shifts.
    """
    base = volume * close.pct_change(14)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def vapr_491_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 112 volume at price over a 5d horizon to identify extreme regimes.
    """
    base = volume * close.pct_change(15)
    return _rolling_mean(base, 5)

def vapr_492_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 112 volume at price over a 21d horizon to identify extreme regimes.
    """
    base = volume * close.pct_change(15)
    return _rolling_mean(base, 21)

def vapr_493_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 112 volume at price over a 63d horizon to identify extreme regimes.
    """
    base = volume * close.pct_change(15)
    return _rolling_mean(base, 63)

def vapr_494_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 112 volume at price over a 126d horizon to identify extreme regimes.
    """
    base = volume * close.pct_change(15)
    return _rolling_mean(base, 126)

def vapr_495_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 112 volume at price over a 252d horizon to identify extreme regimes.
    """
    base = volume * close.pct_change(15)
    return _rolling_mean(base, 252)

def vapr_496_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 112 volume at price by measuring deviations from the 5d mean.
    """
    base = volume * close.pct_change(15)
    return _zscore_rolling(base, 5)

def vapr_497_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 112 volume at price by measuring deviations from the 21d mean.
    """
    base = volume * close.pct_change(15)
    return _zscore_rolling(base, 21)

def vapr_498_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 112 volume at price by measuring deviations from the 63d mean.
    """
    base = volume * close.pct_change(15)
    return _zscore_rolling(base, 63)

def vapr_499_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 112 volume at price by measuring deviations from the 126d mean.
    """
    base = volume * close.pct_change(15)
    return _zscore_rolling(base, 126)

def vapr_500_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 112 volume at price by measuring deviations from the 252d mean.
    """
    base = volume * close.pct_change(15)
    return _zscore_rolling(base, 252)

def vapr_501_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 112 volume at price to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = volume * close.pct_change(15)
    return _rank_pct(base, 5)

def vapr_502_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 112 volume at price to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = volume * close.pct_change(15)
    return _rank_pct(base, 21)

def vapr_503_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 112 volume at price to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = volume * close.pct_change(15)
    return _rank_pct(base, 63)

def vapr_504_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 112 volume at price to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = volume * close.pct_change(15)
    return _rank_pct(base, 126)

def vapr_505_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 112 volume at price to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = volume * close.pct_change(15)
    return _rank_pct(base, 252)

def vapr_506_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 112 volume at price distribution over 5d to detect tail risk or exhaustion.
    """
    base = volume * close.pct_change(15)
    return _rolling_skew(base, 5)

def vapr_507_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 112 volume at price distribution over 21d to detect tail risk or exhaustion.
    """
    base = volume * close.pct_change(15)
    return _rolling_skew(base, 21)

def vapr_508_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 112 volume at price distribution over 63d to detect tail risk or exhaustion.
    """
    base = volume * close.pct_change(15)
    return _rolling_skew(base, 63)

def vapr_509_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 112 volume at price distribution over 126d to detect tail risk or exhaustion.
    """
    base = volume * close.pct_change(15)
    return _rolling_skew(base, 126)

def vapr_510_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 112 volume at price distribution over 252d to detect tail risk or exhaustion.
    """
    base = volume * close.pct_change(15)
    return _rolling_skew(base, 252)

def vapr_511_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 112 volume at price over 5d to capture explosive breakdown or reversal points.
    """
    base = volume * close.pct_change(15)
    return _rolling_kurt(base, 5)

def vapr_512_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 112 volume at price over 21d to capture explosive breakdown or reversal points.
    """
    base = volume * close.pct_change(15)
    return _rolling_kurt(base, 21)

def vapr_513_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 112 volume at price over 63d to capture explosive breakdown or reversal points.
    """
    base = volume * close.pct_change(15)
    return _rolling_kurt(base, 63)

def vapr_514_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 112 volume at price over 126d to capture explosive breakdown or reversal points.
    """
    base = volume * close.pct_change(15)
    return _rolling_kurt(base, 126)

def vapr_515_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 112 volume at price over 252d to capture explosive breakdown or reversal points.
    """
    base = volume * close.pct_change(15)
    return _rolling_kurt(base, 252)

def vapr_516_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 112 volume at price for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = volume * close.pct_change(15)
    return _safe_div(base, _rolling_std(base, 5))

def vapr_517_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 112 volume at price for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = volume * close.pct_change(15)
    return _safe_div(base, _rolling_std(base, 21))

def vapr_518_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 112 volume at price for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = volume * close.pct_change(15)
    return _safe_div(base, _rolling_std(base, 63))

def vapr_519_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 112 volume at price for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = volume * close.pct_change(15)
    return _safe_div(base, _rolling_std(base, 126))

def vapr_520_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 112 volume at price for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = volume * close.pct_change(15)
    return _safe_div(base, _rolling_std(base, 252))

def vapr_521_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 112 volume at price over 5d to stabilize variance and capture exponential shifts.
    """
    base = volume * close.pct_change(15)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def vapr_522_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 112 volume at price over 21d to stabilize variance and capture exponential shifts.
    """
    base = volume * close.pct_change(15)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def vapr_523_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 112 volume at price over 63d to stabilize variance and capture exponential shifts.
    """
    base = volume * close.pct_change(15)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def vapr_524_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 112 volume at price over 126d to stabilize variance and capture exponential shifts.
    """
    base = volume * close.pct_change(15)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def vapr_525_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 112 volume at price over 252d to stabilize variance and capture exponential shifts.
    """
    base = volume * close.pct_change(15)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))
