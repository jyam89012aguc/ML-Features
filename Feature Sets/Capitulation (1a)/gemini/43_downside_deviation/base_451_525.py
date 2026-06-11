"""
43_43_downside_deviation — Base Features 451-525
Domain: 43_downside_deviation
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

def ddev_451_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 43 downside deviation over 5d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(13).rolling(65).mean())
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def ddev_452_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 43 downside deviation over 21d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(13).rolling(65).mean())
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def ddev_453_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 43 downside deviation over 63d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(13).rolling(65).mean())
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def ddev_454_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 43 downside deviation over 126d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(13).rolling(65).mean())
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def ddev_455_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 43 downside deviation over 252d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(13).rolling(65).mean())
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def ddev_456_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 43 downside deviation over a 5d horizon to identify extreme regimes.
    """
    base = (close.pct_change(14).rolling(70).mean())
    return _rolling_mean(base, 5)

def ddev_457_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 43 downside deviation over a 21d horizon to identify extreme regimes.
    """
    base = (close.pct_change(14).rolling(70).mean())
    return _rolling_mean(base, 21)

def ddev_458_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 43 downside deviation over a 63d horizon to identify extreme regimes.
    """
    base = (close.pct_change(14).rolling(70).mean())
    return _rolling_mean(base, 63)

def ddev_459_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 43 downside deviation over a 126d horizon to identify extreme regimes.
    """
    base = (close.pct_change(14).rolling(70).mean())
    return _rolling_mean(base, 126)

def ddev_460_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 43 downside deviation over a 252d horizon to identify extreme regimes.
    """
    base = (close.pct_change(14).rolling(70).mean())
    return _rolling_mean(base, 252)

def ddev_461_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 43 downside deviation by measuring deviations from the 5d mean.
    """
    base = (close.pct_change(14).rolling(70).mean())
    return _zscore_rolling(base, 5)

def ddev_462_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 43 downside deviation by measuring deviations from the 21d mean.
    """
    base = (close.pct_change(14).rolling(70).mean())
    return _zscore_rolling(base, 21)

def ddev_463_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 43 downside deviation by measuring deviations from the 63d mean.
    """
    base = (close.pct_change(14).rolling(70).mean())
    return _zscore_rolling(base, 63)

def ddev_464_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 43 downside deviation by measuring deviations from the 126d mean.
    """
    base = (close.pct_change(14).rolling(70).mean())
    return _zscore_rolling(base, 126)

def ddev_465_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 43 downside deviation by measuring deviations from the 252d mean.
    """
    base = (close.pct_change(14).rolling(70).mean())
    return _zscore_rolling(base, 252)

def ddev_466_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 43 downside deviation to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = (close.pct_change(14).rolling(70).mean())
    return _rank_pct(base, 5)

def ddev_467_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 43 downside deviation to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = (close.pct_change(14).rolling(70).mean())
    return _rank_pct(base, 21)

def ddev_468_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 43 downside deviation to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = (close.pct_change(14).rolling(70).mean())
    return _rank_pct(base, 63)

def ddev_469_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 43 downside deviation to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = (close.pct_change(14).rolling(70).mean())
    return _rank_pct(base, 126)

def ddev_470_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 43 downside deviation to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = (close.pct_change(14).rolling(70).mean())
    return _rank_pct(base, 252)

def ddev_471_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 43 downside deviation distribution over 5d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(14).rolling(70).mean())
    return _rolling_skew(base, 5)

def ddev_472_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 43 downside deviation distribution over 21d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(14).rolling(70).mean())
    return _rolling_skew(base, 21)

def ddev_473_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 43 downside deviation distribution over 63d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(14).rolling(70).mean())
    return _rolling_skew(base, 63)

def ddev_474_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 43 downside deviation distribution over 126d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(14).rolling(70).mean())
    return _rolling_skew(base, 126)

def ddev_475_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 43 downside deviation distribution over 252d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(14).rolling(70).mean())
    return _rolling_skew(base, 252)

def ddev_476_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 43 downside deviation over 5d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(14).rolling(70).mean())
    return _rolling_kurt(base, 5)

def ddev_477_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 43 downside deviation over 21d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(14).rolling(70).mean())
    return _rolling_kurt(base, 21)

def ddev_478_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 43 downside deviation over 63d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(14).rolling(70).mean())
    return _rolling_kurt(base, 63)

def ddev_479_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 43 downside deviation over 126d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(14).rolling(70).mean())
    return _rolling_kurt(base, 126)

def ddev_480_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 43 downside deviation over 252d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(14).rolling(70).mean())
    return _rolling_kurt(base, 252)

def ddev_481_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 43 downside deviation for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(14).rolling(70).mean())
    return _safe_div(base, _rolling_std(base, 5))

def ddev_482_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 43 downside deviation for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(14).rolling(70).mean())
    return _safe_div(base, _rolling_std(base, 21))

def ddev_483_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 43 downside deviation for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(14).rolling(70).mean())
    return _safe_div(base, _rolling_std(base, 63))

def ddev_484_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 43 downside deviation for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(14).rolling(70).mean())
    return _safe_div(base, _rolling_std(base, 126))

def ddev_485_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 43 downside deviation for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(14).rolling(70).mean())
    return _safe_div(base, _rolling_std(base, 252))

def ddev_486_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 43 downside deviation over 5d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(14).rolling(70).mean())
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def ddev_487_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 43 downside deviation over 21d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(14).rolling(70).mean())
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def ddev_488_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 43 downside deviation over 63d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(14).rolling(70).mean())
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def ddev_489_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 43 downside deviation over 126d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(14).rolling(70).mean())
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def ddev_490_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 43 downside deviation over 252d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(14).rolling(70).mean())
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def ddev_491_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 43 downside deviation over a 5d horizon to identify extreme regimes.
    """
    base = (close.pct_change(15).rolling(75).mean())
    return _rolling_mean(base, 5)

def ddev_492_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 43 downside deviation over a 21d horizon to identify extreme regimes.
    """
    base = (close.pct_change(15).rolling(75).mean())
    return _rolling_mean(base, 21)

def ddev_493_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 43 downside deviation over a 63d horizon to identify extreme regimes.
    """
    base = (close.pct_change(15).rolling(75).mean())
    return _rolling_mean(base, 63)

def ddev_494_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 43 downside deviation over a 126d horizon to identify extreme regimes.
    """
    base = (close.pct_change(15).rolling(75).mean())
    return _rolling_mean(base, 126)

def ddev_495_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 43 downside deviation over a 252d horizon to identify extreme regimes.
    """
    base = (close.pct_change(15).rolling(75).mean())
    return _rolling_mean(base, 252)

def ddev_496_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 43 downside deviation by measuring deviations from the 5d mean.
    """
    base = (close.pct_change(15).rolling(75).mean())
    return _zscore_rolling(base, 5)

def ddev_497_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 43 downside deviation by measuring deviations from the 21d mean.
    """
    base = (close.pct_change(15).rolling(75).mean())
    return _zscore_rolling(base, 21)

def ddev_498_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 43 downside deviation by measuring deviations from the 63d mean.
    """
    base = (close.pct_change(15).rolling(75).mean())
    return _zscore_rolling(base, 63)

def ddev_499_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 43 downside deviation by measuring deviations from the 126d mean.
    """
    base = (close.pct_change(15).rolling(75).mean())
    return _zscore_rolling(base, 126)

def ddev_500_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 43 downside deviation by measuring deviations from the 252d mean.
    """
    base = (close.pct_change(15).rolling(75).mean())
    return _zscore_rolling(base, 252)

def ddev_501_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 43 downside deviation to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = (close.pct_change(15).rolling(75).mean())
    return _rank_pct(base, 5)

def ddev_502_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 43 downside deviation to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = (close.pct_change(15).rolling(75).mean())
    return _rank_pct(base, 21)

def ddev_503_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 43 downside deviation to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = (close.pct_change(15).rolling(75).mean())
    return _rank_pct(base, 63)

def ddev_504_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 43 downside deviation to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = (close.pct_change(15).rolling(75).mean())
    return _rank_pct(base, 126)

def ddev_505_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 43 downside deviation to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = (close.pct_change(15).rolling(75).mean())
    return _rank_pct(base, 252)

def ddev_506_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 43 downside deviation distribution over 5d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(15).rolling(75).mean())
    return _rolling_skew(base, 5)

def ddev_507_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 43 downside deviation distribution over 21d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(15).rolling(75).mean())
    return _rolling_skew(base, 21)

def ddev_508_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 43 downside deviation distribution over 63d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(15).rolling(75).mean())
    return _rolling_skew(base, 63)

def ddev_509_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 43 downside deviation distribution over 126d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(15).rolling(75).mean())
    return _rolling_skew(base, 126)

def ddev_510_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 43 downside deviation distribution over 252d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(15).rolling(75).mean())
    return _rolling_skew(base, 252)

def ddev_511_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 43 downside deviation over 5d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(15).rolling(75).mean())
    return _rolling_kurt(base, 5)

def ddev_512_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 43 downside deviation over 21d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(15).rolling(75).mean())
    return _rolling_kurt(base, 21)

def ddev_513_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 43 downside deviation over 63d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(15).rolling(75).mean())
    return _rolling_kurt(base, 63)

def ddev_514_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 43 downside deviation over 126d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(15).rolling(75).mean())
    return _rolling_kurt(base, 126)

def ddev_515_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 43 downside deviation over 252d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(15).rolling(75).mean())
    return _rolling_kurt(base, 252)

def ddev_516_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 43 downside deviation for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(15).rolling(75).mean())
    return _safe_div(base, _rolling_std(base, 5))

def ddev_517_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 43 downside deviation for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(15).rolling(75).mean())
    return _safe_div(base, _rolling_std(base, 21))

def ddev_518_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 43 downside deviation for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(15).rolling(75).mean())
    return _safe_div(base, _rolling_std(base, 63))

def ddev_519_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 43 downside deviation for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(15).rolling(75).mean())
    return _safe_div(base, _rolling_std(base, 126))

def ddev_520_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 43 downside deviation for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(15).rolling(75).mean())
    return _safe_div(base, _rolling_std(base, 252))

def ddev_521_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 43 downside deviation over 5d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(15).rolling(75).mean())
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def ddev_522_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 43 downside deviation over 21d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(15).rolling(75).mean())
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def ddev_523_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 43 downside deviation over 63d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(15).rolling(75).mean())
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def ddev_524_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 43 downside deviation over 126d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(15).rolling(75).mean())
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def ddev_525_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 43 downside deviation over 252d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(15).rolling(75).mean())
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))
