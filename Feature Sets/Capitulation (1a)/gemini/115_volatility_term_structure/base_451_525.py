"""
115_115_volatility_term_structure — Base Features 451-525
Domain: 115_volatility_term_structure
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

def vts_451_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 115 volatility term structure over 5d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(65).std()
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def vts_452_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 115 volatility term structure over 21d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(65).std()
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def vts_453_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 115 volatility term structure over 63d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(65).std()
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def vts_454_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 115 volatility term structure over 126d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(65).std()
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def vts_455_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 115 volatility term structure over 252d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(65).std()
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def vts_456_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 115 volatility term structure over a 5d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(70).std()
    return _rolling_mean(base, 5)

def vts_457_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 115 volatility term structure over a 21d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(70).std()
    return _rolling_mean(base, 21)

def vts_458_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 115 volatility term structure over a 63d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(70).std()
    return _rolling_mean(base, 63)

def vts_459_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 115 volatility term structure over a 126d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(70).std()
    return _rolling_mean(base, 126)

def vts_460_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 115 volatility term structure over a 252d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(70).std()
    return _rolling_mean(base, 252)

def vts_461_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 115 volatility term structure by measuring deviations from the 5d mean.
    """
    base = close.pct_change().rolling(70).std()
    return _zscore_rolling(base, 5)

def vts_462_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 115 volatility term structure by measuring deviations from the 21d mean.
    """
    base = close.pct_change().rolling(70).std()
    return _zscore_rolling(base, 21)

def vts_463_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 115 volatility term structure by measuring deviations from the 63d mean.
    """
    base = close.pct_change().rolling(70).std()
    return _zscore_rolling(base, 63)

def vts_464_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 115 volatility term structure by measuring deviations from the 126d mean.
    """
    base = close.pct_change().rolling(70).std()
    return _zscore_rolling(base, 126)

def vts_465_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 115 volatility term structure by measuring deviations from the 252d mean.
    """
    base = close.pct_change().rolling(70).std()
    return _zscore_rolling(base, 252)

def vts_466_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 115 volatility term structure to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(70).std()
    return _rank_pct(base, 5)

def vts_467_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 115 volatility term structure to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(70).std()
    return _rank_pct(base, 21)

def vts_468_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 115 volatility term structure to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(70).std()
    return _rank_pct(base, 63)

def vts_469_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 115 volatility term structure to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(70).std()
    return _rank_pct(base, 126)

def vts_470_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 115 volatility term structure to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(70).std()
    return _rank_pct(base, 252)

def vts_471_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 115 volatility term structure distribution over 5d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(70).std()
    return _rolling_skew(base, 5)

def vts_472_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 115 volatility term structure distribution over 21d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(70).std()
    return _rolling_skew(base, 21)

def vts_473_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 115 volatility term structure distribution over 63d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(70).std()
    return _rolling_skew(base, 63)

def vts_474_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 115 volatility term structure distribution over 126d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(70).std()
    return _rolling_skew(base, 126)

def vts_475_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 115 volatility term structure distribution over 252d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(70).std()
    return _rolling_skew(base, 252)

def vts_476_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 115 volatility term structure over 5d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(70).std()
    return _rolling_kurt(base, 5)

def vts_477_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 115 volatility term structure over 21d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(70).std()
    return _rolling_kurt(base, 21)

def vts_478_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 115 volatility term structure over 63d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(70).std()
    return _rolling_kurt(base, 63)

def vts_479_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 115 volatility term structure over 126d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(70).std()
    return _rolling_kurt(base, 126)

def vts_480_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 115 volatility term structure over 252d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(70).std()
    return _rolling_kurt(base, 252)

def vts_481_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 115 volatility term structure for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(70).std()
    return _safe_div(base, _rolling_std(base, 5))

def vts_482_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 115 volatility term structure for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(70).std()
    return _safe_div(base, _rolling_std(base, 21))

def vts_483_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 115 volatility term structure for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(70).std()
    return _safe_div(base, _rolling_std(base, 63))

def vts_484_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 115 volatility term structure for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(70).std()
    return _safe_div(base, _rolling_std(base, 126))

def vts_485_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 115 volatility term structure for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(70).std()
    return _safe_div(base, _rolling_std(base, 252))

def vts_486_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 115 volatility term structure over 5d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(70).std()
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def vts_487_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 115 volatility term structure over 21d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(70).std()
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def vts_488_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 115 volatility term structure over 63d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(70).std()
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def vts_489_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 115 volatility term structure over 126d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(70).std()
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def vts_490_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 115 volatility term structure over 252d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(70).std()
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def vts_491_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 115 volatility term structure over a 5d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(75).std()
    return _rolling_mean(base, 5)

def vts_492_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 115 volatility term structure over a 21d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(75).std()
    return _rolling_mean(base, 21)

def vts_493_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 115 volatility term structure over a 63d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(75).std()
    return _rolling_mean(base, 63)

def vts_494_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 115 volatility term structure over a 126d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(75).std()
    return _rolling_mean(base, 126)

def vts_495_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 115 volatility term structure over a 252d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(75).std()
    return _rolling_mean(base, 252)

def vts_496_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 115 volatility term structure by measuring deviations from the 5d mean.
    """
    base = close.pct_change().rolling(75).std()
    return _zscore_rolling(base, 5)

def vts_497_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 115 volatility term structure by measuring deviations from the 21d mean.
    """
    base = close.pct_change().rolling(75).std()
    return _zscore_rolling(base, 21)

def vts_498_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 115 volatility term structure by measuring deviations from the 63d mean.
    """
    base = close.pct_change().rolling(75).std()
    return _zscore_rolling(base, 63)

def vts_499_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 115 volatility term structure by measuring deviations from the 126d mean.
    """
    base = close.pct_change().rolling(75).std()
    return _zscore_rolling(base, 126)

def vts_500_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 115 volatility term structure by measuring deviations from the 252d mean.
    """
    base = close.pct_change().rolling(75).std()
    return _zscore_rolling(base, 252)

def vts_501_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 115 volatility term structure to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(75).std()
    return _rank_pct(base, 5)

def vts_502_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 115 volatility term structure to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(75).std()
    return _rank_pct(base, 21)

def vts_503_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 115 volatility term structure to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(75).std()
    return _rank_pct(base, 63)

def vts_504_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 115 volatility term structure to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(75).std()
    return _rank_pct(base, 126)

def vts_505_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 115 volatility term structure to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(75).std()
    return _rank_pct(base, 252)

def vts_506_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 115 volatility term structure distribution over 5d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(75).std()
    return _rolling_skew(base, 5)

def vts_507_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 115 volatility term structure distribution over 21d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(75).std()
    return _rolling_skew(base, 21)

def vts_508_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 115 volatility term structure distribution over 63d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(75).std()
    return _rolling_skew(base, 63)

def vts_509_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 115 volatility term structure distribution over 126d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(75).std()
    return _rolling_skew(base, 126)

def vts_510_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 115 volatility term structure distribution over 252d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(75).std()
    return _rolling_skew(base, 252)

def vts_511_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 115 volatility term structure over 5d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(75).std()
    return _rolling_kurt(base, 5)

def vts_512_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 115 volatility term structure over 21d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(75).std()
    return _rolling_kurt(base, 21)

def vts_513_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 115 volatility term structure over 63d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(75).std()
    return _rolling_kurt(base, 63)

def vts_514_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 115 volatility term structure over 126d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(75).std()
    return _rolling_kurt(base, 126)

def vts_515_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 115 volatility term structure over 252d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(75).std()
    return _rolling_kurt(base, 252)

def vts_516_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 115 volatility term structure for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(75).std()
    return _safe_div(base, _rolling_std(base, 5))

def vts_517_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 115 volatility term structure for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(75).std()
    return _safe_div(base, _rolling_std(base, 21))

def vts_518_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 115 volatility term structure for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(75).std()
    return _safe_div(base, _rolling_std(base, 63))

def vts_519_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 115 volatility term structure for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(75).std()
    return _safe_div(base, _rolling_std(base, 126))

def vts_520_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 115 volatility term structure for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(75).std()
    return _safe_div(base, _rolling_std(base, 252))

def vts_521_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 115 volatility term structure over 5d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(75).std()
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def vts_522_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 115 volatility term structure over 21d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(75).std()
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def vts_523_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 115 volatility term structure over 63d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(75).std()
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def vts_524_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 115 volatility term structure over 126d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(75).std()
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def vts_525_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 115 volatility term structure over 252d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(75).std()
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))
