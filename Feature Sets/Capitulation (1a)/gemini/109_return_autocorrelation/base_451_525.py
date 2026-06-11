"""
109_109_return_autocorrelation — Base Features 451-525
Domain: 109_return_autocorrelation
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

def raut_451_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 109 return autocorrelation over 5d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=13), raw=True)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def raut_452_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 109 return autocorrelation over 21d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=13), raw=True)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def raut_453_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 109 return autocorrelation over 63d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=13), raw=True)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def raut_454_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 109 return autocorrelation over 126d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=13), raw=True)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def raut_455_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 109 return autocorrelation over 252d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=13), raw=True)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def raut_456_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 109 return autocorrelation over a 5d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=14), raw=True)
    return _rolling_mean(base, 5)

def raut_457_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 109 return autocorrelation over a 21d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=14), raw=True)
    return _rolling_mean(base, 21)

def raut_458_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 109 return autocorrelation over a 63d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=14), raw=True)
    return _rolling_mean(base, 63)

def raut_459_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 109 return autocorrelation over a 126d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=14), raw=True)
    return _rolling_mean(base, 126)

def raut_460_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 109 return autocorrelation over a 252d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=14), raw=True)
    return _rolling_mean(base, 252)

def raut_461_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 109 return autocorrelation by measuring deviations from the 5d mean.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=14), raw=True)
    return _zscore_rolling(base, 5)

def raut_462_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 109 return autocorrelation by measuring deviations from the 21d mean.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=14), raw=True)
    return _zscore_rolling(base, 21)

def raut_463_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 109 return autocorrelation by measuring deviations from the 63d mean.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=14), raw=True)
    return _zscore_rolling(base, 63)

def raut_464_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 109 return autocorrelation by measuring deviations from the 126d mean.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=14), raw=True)
    return _zscore_rolling(base, 126)

def raut_465_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 109 return autocorrelation by measuring deviations from the 252d mean.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=14), raw=True)
    return _zscore_rolling(base, 252)

def raut_466_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 109 return autocorrelation to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=14), raw=True)
    return _rank_pct(base, 5)

def raut_467_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 109 return autocorrelation to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=14), raw=True)
    return _rank_pct(base, 21)

def raut_468_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 109 return autocorrelation to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=14), raw=True)
    return _rank_pct(base, 63)

def raut_469_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 109 return autocorrelation to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=14), raw=True)
    return _rank_pct(base, 126)

def raut_470_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 109 return autocorrelation to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=14), raw=True)
    return _rank_pct(base, 252)

def raut_471_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 109 return autocorrelation distribution over 5d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=14), raw=True)
    return _rolling_skew(base, 5)

def raut_472_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 109 return autocorrelation distribution over 21d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=14), raw=True)
    return _rolling_skew(base, 21)

def raut_473_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 109 return autocorrelation distribution over 63d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=14), raw=True)
    return _rolling_skew(base, 63)

def raut_474_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 109 return autocorrelation distribution over 126d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=14), raw=True)
    return _rolling_skew(base, 126)

def raut_475_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 109 return autocorrelation distribution over 252d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=14), raw=True)
    return _rolling_skew(base, 252)

def raut_476_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 109 return autocorrelation over 5d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=14), raw=True)
    return _rolling_kurt(base, 5)

def raut_477_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 109 return autocorrelation over 21d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=14), raw=True)
    return _rolling_kurt(base, 21)

def raut_478_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 109 return autocorrelation over 63d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=14), raw=True)
    return _rolling_kurt(base, 63)

def raut_479_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 109 return autocorrelation over 126d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=14), raw=True)
    return _rolling_kurt(base, 126)

def raut_480_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 109 return autocorrelation over 252d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=14), raw=True)
    return _rolling_kurt(base, 252)

def raut_481_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 109 return autocorrelation for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=14), raw=True)
    return _safe_div(base, _rolling_std(base, 5))

def raut_482_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 109 return autocorrelation for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=14), raw=True)
    return _safe_div(base, _rolling_std(base, 21))

def raut_483_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 109 return autocorrelation for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=14), raw=True)
    return _safe_div(base, _rolling_std(base, 63))

def raut_484_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 109 return autocorrelation for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=14), raw=True)
    return _safe_div(base, _rolling_std(base, 126))

def raut_485_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 109 return autocorrelation for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=14), raw=True)
    return _safe_div(base, _rolling_std(base, 252))

def raut_486_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 109 return autocorrelation over 5d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=14), raw=True)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def raut_487_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 109 return autocorrelation over 21d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=14), raw=True)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def raut_488_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 109 return autocorrelation over 63d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=14), raw=True)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def raut_489_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 109 return autocorrelation over 126d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=14), raw=True)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def raut_490_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 109 return autocorrelation over 252d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=14), raw=True)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def raut_491_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 109 return autocorrelation over a 5d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=15), raw=True)
    return _rolling_mean(base, 5)

def raut_492_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 109 return autocorrelation over a 21d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=15), raw=True)
    return _rolling_mean(base, 21)

def raut_493_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 109 return autocorrelation over a 63d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=15), raw=True)
    return _rolling_mean(base, 63)

def raut_494_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 109 return autocorrelation over a 126d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=15), raw=True)
    return _rolling_mean(base, 126)

def raut_495_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 109 return autocorrelation over a 252d horizon to identify extreme regimes.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=15), raw=True)
    return _rolling_mean(base, 252)

def raut_496_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 109 return autocorrelation by measuring deviations from the 5d mean.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=15), raw=True)
    return _zscore_rolling(base, 5)

def raut_497_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 109 return autocorrelation by measuring deviations from the 21d mean.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=15), raw=True)
    return _zscore_rolling(base, 21)

def raut_498_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 109 return autocorrelation by measuring deviations from the 63d mean.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=15), raw=True)
    return _zscore_rolling(base, 63)

def raut_499_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 109 return autocorrelation by measuring deviations from the 126d mean.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=15), raw=True)
    return _zscore_rolling(base, 126)

def raut_500_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 109 return autocorrelation by measuring deviations from the 252d mean.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=15), raw=True)
    return _zscore_rolling(base, 252)

def raut_501_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 109 return autocorrelation to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=15), raw=True)
    return _rank_pct(base, 5)

def raut_502_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 109 return autocorrelation to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=15), raw=True)
    return _rank_pct(base, 21)

def raut_503_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 109 return autocorrelation to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=15), raw=True)
    return _rank_pct(base, 63)

def raut_504_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 109 return autocorrelation to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=15), raw=True)
    return _rank_pct(base, 126)

def raut_505_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 109 return autocorrelation to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=15), raw=True)
    return _rank_pct(base, 252)

def raut_506_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 109 return autocorrelation distribution over 5d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=15), raw=True)
    return _rolling_skew(base, 5)

def raut_507_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 109 return autocorrelation distribution over 21d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=15), raw=True)
    return _rolling_skew(base, 21)

def raut_508_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 109 return autocorrelation distribution over 63d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=15), raw=True)
    return _rolling_skew(base, 63)

def raut_509_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 109 return autocorrelation distribution over 126d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=15), raw=True)
    return _rolling_skew(base, 126)

def raut_510_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 109 return autocorrelation distribution over 252d to detect tail risk or exhaustion.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=15), raw=True)
    return _rolling_skew(base, 252)

def raut_511_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 109 return autocorrelation over 5d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=15), raw=True)
    return _rolling_kurt(base, 5)

def raut_512_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 109 return autocorrelation over 21d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=15), raw=True)
    return _rolling_kurt(base, 21)

def raut_513_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 109 return autocorrelation over 63d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=15), raw=True)
    return _rolling_kurt(base, 63)

def raut_514_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 109 return autocorrelation over 126d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=15), raw=True)
    return _rolling_kurt(base, 126)

def raut_515_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 109 return autocorrelation over 252d to capture explosive breakdown or reversal points.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=15), raw=True)
    return _rolling_kurt(base, 252)

def raut_516_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 109 return autocorrelation for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=15), raw=True)
    return _safe_div(base, _rolling_std(base, 5))

def raut_517_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 109 return autocorrelation for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=15), raw=True)
    return _safe_div(base, _rolling_std(base, 21))

def raut_518_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 109 return autocorrelation for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=15), raw=True)
    return _safe_div(base, _rolling_std(base, 63))

def raut_519_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 109 return autocorrelation for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=15), raw=True)
    return _safe_div(base, _rolling_std(base, 126))

def raut_520_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 109 return autocorrelation for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=15), raw=True)
    return _safe_div(base, _rolling_std(base, 252))

def raut_521_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 109 return autocorrelation over 5d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=15), raw=True)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def raut_522_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 109 return autocorrelation over 21d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=15), raw=True)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def raut_523_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 109 return autocorrelation over 63d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=15), raw=True)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def raut_524_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 109 return autocorrelation over 126d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=15), raw=True)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def raut_525_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 109 return autocorrelation over 252d to stabilize variance and capture exponential shifts.
    """
    base = close.pct_change().rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=15), raw=True)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))
