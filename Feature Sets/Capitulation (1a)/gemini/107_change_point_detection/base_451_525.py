"""
107_107_change_point_detection — Base Features 451-525
Domain: 107_change_point_detection
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

def cpdt_451_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 107 change point detection over 5d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(65).std().diff()
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def cpdt_452_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 107 change point detection over 21d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(65).std().diff()
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def cpdt_453_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 107 change point detection over 63d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(65).std().diff()
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def cpdt_454_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 107 change point detection over 126d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(65).std().diff()
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def cpdt_455_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 107 change point detection over 252d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(65).std().diff()
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def cpdt_456_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 107 change point detection over a 5d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(70).std().diff()
    return _rolling_mean(base, 5)

def cpdt_457_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 107 change point detection over a 21d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(70).std().diff()
    return _rolling_mean(base, 21)

def cpdt_458_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 107 change point detection over a 63d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(70).std().diff()
    return _rolling_mean(base, 63)

def cpdt_459_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 107 change point detection over a 126d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(70).std().diff()
    return _rolling_mean(base, 126)

def cpdt_460_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 107 change point detection over a 252d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(70).std().diff()
    return _rolling_mean(base, 252)

def cpdt_461_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 107 change point detection by measuring deviations from the 5d mean.
    """
    base = close.pct_change().rolling(70).std().diff()
    return _zscore_rolling(base, 5)

def cpdt_462_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 107 change point detection by measuring deviations from the 21d mean.
    """
    base = close.pct_change().rolling(70).std().diff()
    return _zscore_rolling(base, 21)

def cpdt_463_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 107 change point detection by measuring deviations from the 63d mean.
    """
    base = close.pct_change().rolling(70).std().diff()
    return _zscore_rolling(base, 63)

def cpdt_464_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 107 change point detection by measuring deviations from the 126d mean.
    """
    base = close.pct_change().rolling(70).std().diff()
    return _zscore_rolling(base, 126)

def cpdt_465_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 107 change point detection by measuring deviations from the 252d mean.
    """
    base = close.pct_change().rolling(70).std().diff()
    return _zscore_rolling(base, 252)

def cpdt_466_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 107 change point detection to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(70).std().diff()
    return _rank_pct(base, 5)

def cpdt_467_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 107 change point detection to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(70).std().diff()
    return _rank_pct(base, 21)

def cpdt_468_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 107 change point detection to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(70).std().diff()
    return _rank_pct(base, 63)

def cpdt_469_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 107 change point detection to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(70).std().diff()
    return _rank_pct(base, 126)

def cpdt_470_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 107 change point detection to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(70).std().diff()
    return _rank_pct(base, 252)

def cpdt_471_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 107 change point detection distribution over 5d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(70).std().diff()
    return _rolling_skew(base, 5)

def cpdt_472_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 107 change point detection distribution over 21d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(70).std().diff()
    return _rolling_skew(base, 21)

def cpdt_473_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 107 change point detection distribution over 63d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(70).std().diff()
    return _rolling_skew(base, 63)

def cpdt_474_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 107 change point detection distribution over 126d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(70).std().diff()
    return _rolling_skew(base, 126)

def cpdt_475_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 107 change point detection distribution over 252d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(70).std().diff()
    return _rolling_skew(base, 252)

def cpdt_476_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 107 change point detection over 5d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(70).std().diff()
    return _rolling_kurt(base, 5)

def cpdt_477_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 107 change point detection over 21d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(70).std().diff()
    return _rolling_kurt(base, 21)

def cpdt_478_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 107 change point detection over 63d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(70).std().diff()
    return _rolling_kurt(base, 63)

def cpdt_479_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 107 change point detection over 126d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(70).std().diff()
    return _rolling_kurt(base, 126)

def cpdt_480_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 107 change point detection over 252d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(70).std().diff()
    return _rolling_kurt(base, 252)

def cpdt_481_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 107 change point detection for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(70).std().diff()
    return _safe_div(base, _rolling_std(base, 5))

def cpdt_482_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 107 change point detection for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(70).std().diff()
    return _safe_div(base, _rolling_std(base, 21))

def cpdt_483_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 107 change point detection for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(70).std().diff()
    return _safe_div(base, _rolling_std(base, 63))

def cpdt_484_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 107 change point detection for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(70).std().diff()
    return _safe_div(base, _rolling_std(base, 126))

def cpdt_485_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 107 change point detection for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(70).std().diff()
    return _safe_div(base, _rolling_std(base, 252))

def cpdt_486_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 107 change point detection over 5d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(70).std().diff()
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def cpdt_487_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 107 change point detection over 21d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(70).std().diff()
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def cpdt_488_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 107 change point detection over 63d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(70).std().diff()
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def cpdt_489_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 107 change point detection over 126d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(70).std().diff()
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def cpdt_490_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 107 change point detection over 252d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(70).std().diff()
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def cpdt_491_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 107 change point detection over a 5d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(75).std().diff()
    return _rolling_mean(base, 5)

def cpdt_492_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 107 change point detection over a 21d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(75).std().diff()
    return _rolling_mean(base, 21)

def cpdt_493_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 107 change point detection over a 63d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(75).std().diff()
    return _rolling_mean(base, 63)

def cpdt_494_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 107 change point detection over a 126d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(75).std().diff()
    return _rolling_mean(base, 126)

def cpdt_495_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 107 change point detection over a 252d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(75).std().diff()
    return _rolling_mean(base, 252)

def cpdt_496_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 107 change point detection by measuring deviations from the 5d mean.
    """
    base = close.pct_change().rolling(75).std().diff()
    return _zscore_rolling(base, 5)

def cpdt_497_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 107 change point detection by measuring deviations from the 21d mean.
    """
    base = close.pct_change().rolling(75).std().diff()
    return _zscore_rolling(base, 21)

def cpdt_498_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 107 change point detection by measuring deviations from the 63d mean.
    """
    base = close.pct_change().rolling(75).std().diff()
    return _zscore_rolling(base, 63)

def cpdt_499_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 107 change point detection by measuring deviations from the 126d mean.
    """
    base = close.pct_change().rolling(75).std().diff()
    return _zscore_rolling(base, 126)

def cpdt_500_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 107 change point detection by measuring deviations from the 252d mean.
    """
    base = close.pct_change().rolling(75).std().diff()
    return _zscore_rolling(base, 252)

def cpdt_501_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 107 change point detection to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(75).std().diff()
    return _rank_pct(base, 5)

def cpdt_502_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 107 change point detection to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(75).std().diff()
    return _rank_pct(base, 21)

def cpdt_503_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 107 change point detection to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(75).std().diff()
    return _rank_pct(base, 63)

def cpdt_504_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 107 change point detection to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(75).std().diff()
    return _rank_pct(base, 126)

def cpdt_505_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 107 change point detection to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(75).std().diff()
    return _rank_pct(base, 252)

def cpdt_506_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 107 change point detection distribution over 5d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(75).std().diff()
    return _rolling_skew(base, 5)

def cpdt_507_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 107 change point detection distribution over 21d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(75).std().diff()
    return _rolling_skew(base, 21)

def cpdt_508_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 107 change point detection distribution over 63d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(75).std().diff()
    return _rolling_skew(base, 63)

def cpdt_509_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 107 change point detection distribution over 126d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(75).std().diff()
    return _rolling_skew(base, 126)

def cpdt_510_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 107 change point detection distribution over 252d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(75).std().diff()
    return _rolling_skew(base, 252)

def cpdt_511_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 107 change point detection over 5d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(75).std().diff()
    return _rolling_kurt(base, 5)

def cpdt_512_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 107 change point detection over 21d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(75).std().diff()
    return _rolling_kurt(base, 21)

def cpdt_513_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 107 change point detection over 63d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(75).std().diff()
    return _rolling_kurt(base, 63)

def cpdt_514_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 107 change point detection over 126d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(75).std().diff()
    return _rolling_kurt(base, 126)

def cpdt_515_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 107 change point detection over 252d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(75).std().diff()
    return _rolling_kurt(base, 252)

def cpdt_516_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 107 change point detection for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(75).std().diff()
    return _safe_div(base, _rolling_std(base, 5))

def cpdt_517_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 107 change point detection for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(75).std().diff()
    return _safe_div(base, _rolling_std(base, 21))

def cpdt_518_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 107 change point detection for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(75).std().diff()
    return _safe_div(base, _rolling_std(base, 63))

def cpdt_519_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 107 change point detection for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(75).std().diff()
    return _safe_div(base, _rolling_std(base, 126))

def cpdt_520_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 107 change point detection for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(75).std().diff()
    return _safe_div(base, _rolling_std(base, 252))

def cpdt_521_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 107 change point detection over 5d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(75).std().diff()
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def cpdt_522_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 107 change point detection over 21d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(75).std().diff()
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def cpdt_523_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 107 change point detection over 63d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(75).std().diff()
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def cpdt_524_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 107 change point detection over 126d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(75).std().diff()
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def cpdt_525_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 107 change point detection over 252d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(75).std().diff()
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))
