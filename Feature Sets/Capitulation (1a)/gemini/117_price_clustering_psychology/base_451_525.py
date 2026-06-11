"""
117_117_price_clustering_psychology — Base Features 451-525
Domain: 117_price_clustering_psychology
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

def ppsy_451_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 117 price clustering psychology over 5d to stabilize variance and capture exponential shifts.
    """
    base = np.abs(close - close.rolling(65).mean())
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def ppsy_452_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 117 price clustering psychology over 21d to stabilize variance and capture exponential shifts.
    """
    base = np.abs(close - close.rolling(65).mean())
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def ppsy_453_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 117 price clustering psychology over 63d to stabilize variance and capture exponential shifts.
    """
    base = np.abs(close - close.rolling(65).mean())
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def ppsy_454_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 117 price clustering psychology over 126d to stabilize variance and capture exponential shifts.
    """
    base = np.abs(close - close.rolling(65).mean())
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def ppsy_455_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 117 price clustering psychology over 252d to stabilize variance and capture exponential shifts.
    """
    base = np.abs(close - close.rolling(65).mean())
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def ppsy_456_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 117 price clustering psychology over a 5d horizon to identify extreme regimes.
    """
    base = np.abs(close - close.rolling(70).mean())
    return _rolling_mean(base, 5)

def ppsy_457_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 117 price clustering psychology over a 21d horizon to identify extreme regimes.
    """
    base = np.abs(close - close.rolling(70).mean())
    return _rolling_mean(base, 21)

def ppsy_458_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 117 price clustering psychology over a 63d horizon to identify extreme regimes.
    """
    base = np.abs(close - close.rolling(70).mean())
    return _rolling_mean(base, 63)

def ppsy_459_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 117 price clustering psychology over a 126d horizon to identify extreme regimes.
    """
    base = np.abs(close - close.rolling(70).mean())
    return _rolling_mean(base, 126)

def ppsy_460_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 117 price clustering psychology over a 252d horizon to identify extreme regimes.
    """
    base = np.abs(close - close.rolling(70).mean())
    return _rolling_mean(base, 252)

def ppsy_461_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 117 price clustering psychology by measuring deviations from the 5d mean.
    """
    base = np.abs(close - close.rolling(70).mean())
    return _zscore_rolling(base, 5)

def ppsy_462_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 117 price clustering psychology by measuring deviations from the 21d mean.
    """
    base = np.abs(close - close.rolling(70).mean())
    return _zscore_rolling(base, 21)

def ppsy_463_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 117 price clustering psychology by measuring deviations from the 63d mean.
    """
    base = np.abs(close - close.rolling(70).mean())
    return _zscore_rolling(base, 63)

def ppsy_464_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 117 price clustering psychology by measuring deviations from the 126d mean.
    """
    base = np.abs(close - close.rolling(70).mean())
    return _zscore_rolling(base, 126)

def ppsy_465_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 117 price clustering psychology by measuring deviations from the 252d mean.
    """
    base = np.abs(close - close.rolling(70).mean())
    return _zscore_rolling(base, 252)

def ppsy_466_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 117 price clustering psychology to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = np.abs(close - close.rolling(70).mean())
    return _rank_pct(base, 5)

def ppsy_467_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 117 price clustering psychology to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = np.abs(close - close.rolling(70).mean())
    return _rank_pct(base, 21)

def ppsy_468_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 117 price clustering psychology to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = np.abs(close - close.rolling(70).mean())
    return _rank_pct(base, 63)

def ppsy_469_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 117 price clustering psychology to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = np.abs(close - close.rolling(70).mean())
    return _rank_pct(base, 126)

def ppsy_470_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 117 price clustering psychology to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = np.abs(close - close.rolling(70).mean())
    return _rank_pct(base, 252)

def ppsy_471_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 117 price clustering psychology distribution over 5d to detect tail risk or exhaustion.
    """
    base = np.abs(close - close.rolling(70).mean())
    return _rolling_skew(base, 5)

def ppsy_472_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 117 price clustering psychology distribution over 21d to detect tail risk or exhaustion.
    """
    base = np.abs(close - close.rolling(70).mean())
    return _rolling_skew(base, 21)

def ppsy_473_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 117 price clustering psychology distribution over 63d to detect tail risk or exhaustion.
    """
    base = np.abs(close - close.rolling(70).mean())
    return _rolling_skew(base, 63)

def ppsy_474_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 117 price clustering psychology distribution over 126d to detect tail risk or exhaustion.
    """
    base = np.abs(close - close.rolling(70).mean())
    return _rolling_skew(base, 126)

def ppsy_475_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 117 price clustering psychology distribution over 252d to detect tail risk or exhaustion.
    """
    base = np.abs(close - close.rolling(70).mean())
    return _rolling_skew(base, 252)

def ppsy_476_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 117 price clustering psychology over 5d to capture explosive breakdown or reversal points.
    """
    base = np.abs(close - close.rolling(70).mean())
    return _rolling_kurt(base, 5)

def ppsy_477_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 117 price clustering psychology over 21d to capture explosive breakdown or reversal points.
    """
    base = np.abs(close - close.rolling(70).mean())
    return _rolling_kurt(base, 21)

def ppsy_478_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 117 price clustering psychology over 63d to capture explosive breakdown or reversal points.
    """
    base = np.abs(close - close.rolling(70).mean())
    return _rolling_kurt(base, 63)

def ppsy_479_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 117 price clustering psychology over 126d to capture explosive breakdown or reversal points.
    """
    base = np.abs(close - close.rolling(70).mean())
    return _rolling_kurt(base, 126)

def ppsy_480_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 117 price clustering psychology over 252d to capture explosive breakdown or reversal points.
    """
    base = np.abs(close - close.rolling(70).mean())
    return _rolling_kurt(base, 252)

def ppsy_481_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 117 price clustering psychology for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = np.abs(close - close.rolling(70).mean())
    return _safe_div(base, _rolling_std(base, 5))

def ppsy_482_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 117 price clustering psychology for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = np.abs(close - close.rolling(70).mean())
    return _safe_div(base, _rolling_std(base, 21))

def ppsy_483_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 117 price clustering psychology for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = np.abs(close - close.rolling(70).mean())
    return _safe_div(base, _rolling_std(base, 63))

def ppsy_484_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 117 price clustering psychology for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = np.abs(close - close.rolling(70).mean())
    return _safe_div(base, _rolling_std(base, 126))

def ppsy_485_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 117 price clustering psychology for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = np.abs(close - close.rolling(70).mean())
    return _safe_div(base, _rolling_std(base, 252))

def ppsy_486_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 117 price clustering psychology over 5d to stabilize variance and capture exponential shifts.
    """
    base = np.abs(close - close.rolling(70).mean())
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def ppsy_487_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 117 price clustering psychology over 21d to stabilize variance and capture exponential shifts.
    """
    base = np.abs(close - close.rolling(70).mean())
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def ppsy_488_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 117 price clustering psychology over 63d to stabilize variance and capture exponential shifts.
    """
    base = np.abs(close - close.rolling(70).mean())
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def ppsy_489_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 117 price clustering psychology over 126d to stabilize variance and capture exponential shifts.
    """
    base = np.abs(close - close.rolling(70).mean())
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def ppsy_490_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 117 price clustering psychology over 252d to stabilize variance and capture exponential shifts.
    """
    base = np.abs(close - close.rolling(70).mean())
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def ppsy_491_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 117 price clustering psychology over a 5d horizon to identify extreme regimes.
    """
    base = np.abs(close - close.rolling(75).mean())
    return _rolling_mean(base, 5)

def ppsy_492_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 117 price clustering psychology over a 21d horizon to identify extreme regimes.
    """
    base = np.abs(close - close.rolling(75).mean())
    return _rolling_mean(base, 21)

def ppsy_493_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 117 price clustering psychology over a 63d horizon to identify extreme regimes.
    """
    base = np.abs(close - close.rolling(75).mean())
    return _rolling_mean(base, 63)

def ppsy_494_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 117 price clustering psychology over a 126d horizon to identify extreme regimes.
    """
    base = np.abs(close - close.rolling(75).mean())
    return _rolling_mean(base, 126)

def ppsy_495_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 117 price clustering psychology over a 252d horizon to identify extreme regimes.
    """
    base = np.abs(close - close.rolling(75).mean())
    return _rolling_mean(base, 252)

def ppsy_496_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 117 price clustering psychology by measuring deviations from the 5d mean.
    """
    base = np.abs(close - close.rolling(75).mean())
    return _zscore_rolling(base, 5)

def ppsy_497_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 117 price clustering psychology by measuring deviations from the 21d mean.
    """
    base = np.abs(close - close.rolling(75).mean())
    return _zscore_rolling(base, 21)

def ppsy_498_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 117 price clustering psychology by measuring deviations from the 63d mean.
    """
    base = np.abs(close - close.rolling(75).mean())
    return _zscore_rolling(base, 63)

def ppsy_499_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 117 price clustering psychology by measuring deviations from the 126d mean.
    """
    base = np.abs(close - close.rolling(75).mean())
    return _zscore_rolling(base, 126)

def ppsy_500_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 117 price clustering psychology by measuring deviations from the 252d mean.
    """
    base = np.abs(close - close.rolling(75).mean())
    return _zscore_rolling(base, 252)

def ppsy_501_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 117 price clustering psychology to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = np.abs(close - close.rolling(75).mean())
    return _rank_pct(base, 5)

def ppsy_502_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 117 price clustering psychology to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = np.abs(close - close.rolling(75).mean())
    return _rank_pct(base, 21)

def ppsy_503_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 117 price clustering psychology to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = np.abs(close - close.rolling(75).mean())
    return _rank_pct(base, 63)

def ppsy_504_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 117 price clustering psychology to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = np.abs(close - close.rolling(75).mean())
    return _rank_pct(base, 126)

def ppsy_505_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 117 price clustering psychology to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = np.abs(close - close.rolling(75).mean())
    return _rank_pct(base, 252)

def ppsy_506_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 117 price clustering psychology distribution over 5d to detect tail risk or exhaustion.
    """
    base = np.abs(close - close.rolling(75).mean())
    return _rolling_skew(base, 5)

def ppsy_507_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 117 price clustering psychology distribution over 21d to detect tail risk or exhaustion.
    """
    base = np.abs(close - close.rolling(75).mean())
    return _rolling_skew(base, 21)

def ppsy_508_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 117 price clustering psychology distribution over 63d to detect tail risk or exhaustion.
    """
    base = np.abs(close - close.rolling(75).mean())
    return _rolling_skew(base, 63)

def ppsy_509_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 117 price clustering psychology distribution over 126d to detect tail risk or exhaustion.
    """
    base = np.abs(close - close.rolling(75).mean())
    return _rolling_skew(base, 126)

def ppsy_510_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 117 price clustering psychology distribution over 252d to detect tail risk or exhaustion.
    """
    base = np.abs(close - close.rolling(75).mean())
    return _rolling_skew(base, 252)

def ppsy_511_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 117 price clustering psychology over 5d to capture explosive breakdown or reversal points.
    """
    base = np.abs(close - close.rolling(75).mean())
    return _rolling_kurt(base, 5)

def ppsy_512_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 117 price clustering psychology over 21d to capture explosive breakdown or reversal points.
    """
    base = np.abs(close - close.rolling(75).mean())
    return _rolling_kurt(base, 21)

def ppsy_513_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 117 price clustering psychology over 63d to capture explosive breakdown or reversal points.
    """
    base = np.abs(close - close.rolling(75).mean())
    return _rolling_kurt(base, 63)

def ppsy_514_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 117 price clustering psychology over 126d to capture explosive breakdown or reversal points.
    """
    base = np.abs(close - close.rolling(75).mean())
    return _rolling_kurt(base, 126)

def ppsy_515_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 117 price clustering psychology over 252d to capture explosive breakdown or reversal points.
    """
    base = np.abs(close - close.rolling(75).mean())
    return _rolling_kurt(base, 252)

def ppsy_516_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 117 price clustering psychology for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = np.abs(close - close.rolling(75).mean())
    return _safe_div(base, _rolling_std(base, 5))

def ppsy_517_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 117 price clustering psychology for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = np.abs(close - close.rolling(75).mean())
    return _safe_div(base, _rolling_std(base, 21))

def ppsy_518_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 117 price clustering psychology for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = np.abs(close - close.rolling(75).mean())
    return _safe_div(base, _rolling_std(base, 63))

def ppsy_519_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 117 price clustering psychology for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = np.abs(close - close.rolling(75).mean())
    return _safe_div(base, _rolling_std(base, 126))

def ppsy_520_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 117 price clustering psychology for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = np.abs(close - close.rolling(75).mean())
    return _safe_div(base, _rolling_std(base, 252))

def ppsy_521_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 117 price clustering psychology over 5d to stabilize variance and capture exponential shifts.
    """
    base = np.abs(close - close.rolling(75).mean())
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def ppsy_522_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 117 price clustering psychology over 21d to stabilize variance and capture exponential shifts.
    """
    base = np.abs(close - close.rolling(75).mean())
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def ppsy_523_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 117 price clustering psychology over 63d to stabilize variance and capture exponential shifts.
    """
    base = np.abs(close - close.rolling(75).mean())
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def ppsy_524_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 117 price clustering psychology over 126d to stabilize variance and capture exponential shifts.
    """
    base = np.abs(close - close.rolling(75).mean())
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def ppsy_525_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 117 price clustering psychology over 252d to stabilize variance and capture exponential shifts.
    """
    base = np.abs(close - close.rolling(75).mean())
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))
