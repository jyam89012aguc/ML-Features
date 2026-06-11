"""
105_105_fractal_structure — Base Features 451-525
Domain: 105_fractal_structure
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

def frac_451_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 105 fractal structure over 5d to stabilize variance and capture exponential shifts.
    """
    base = close.diff().abs().rolling(65).sum()
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def frac_452_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 105 fractal structure over 21d to stabilize variance and capture exponential shifts.
    """
    base = close.diff().abs().rolling(65).sum()
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def frac_453_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 105 fractal structure over 63d to stabilize variance and capture exponential shifts.
    """
    base = close.diff().abs().rolling(65).sum()
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def frac_454_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 105 fractal structure over 126d to stabilize variance and capture exponential shifts.
    """
    base = close.diff().abs().rolling(65).sum()
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def frac_455_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 105 fractal structure over 252d to stabilize variance and capture exponential shifts.
    """
    base = close.diff().abs().rolling(65).sum()
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def frac_456_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 105 fractal structure over a 5d horizon to identify extreme regimes.
    """
    base = close.diff().abs().rolling(70).sum()
    return _rolling_mean(base, 5)

def frac_457_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 105 fractal structure over a 21d horizon to identify extreme regimes.
    """
    base = close.diff().abs().rolling(70).sum()
    return _rolling_mean(base, 21)

def frac_458_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 105 fractal structure over a 63d horizon to identify extreme regimes.
    """
    base = close.diff().abs().rolling(70).sum()
    return _rolling_mean(base, 63)

def frac_459_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 105 fractal structure over a 126d horizon to identify extreme regimes.
    """
    base = close.diff().abs().rolling(70).sum()
    return _rolling_mean(base, 126)

def frac_460_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 105 fractal structure over a 252d horizon to identify extreme regimes.
    """
    base = close.diff().abs().rolling(70).sum()
    return _rolling_mean(base, 252)

def frac_461_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 105 fractal structure by measuring deviations from the 5d mean.
    """
    base = close.diff().abs().rolling(70).sum()
    return _zscore_rolling(base, 5)

def frac_462_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 105 fractal structure by measuring deviations from the 21d mean.
    """
    base = close.diff().abs().rolling(70).sum()
    return _zscore_rolling(base, 21)

def frac_463_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 105 fractal structure by measuring deviations from the 63d mean.
    """
    base = close.diff().abs().rolling(70).sum()
    return _zscore_rolling(base, 63)

def frac_464_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 105 fractal structure by measuring deviations from the 126d mean.
    """
    base = close.diff().abs().rolling(70).sum()
    return _zscore_rolling(base, 126)

def frac_465_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 105 fractal structure by measuring deviations from the 252d mean.
    """
    base = close.diff().abs().rolling(70).sum()
    return _zscore_rolling(base, 252)

def frac_466_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 105 fractal structure to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = close.diff().abs().rolling(70).sum()
    return _rank_pct(base, 5)

def frac_467_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 105 fractal structure to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = close.diff().abs().rolling(70).sum()
    return _rank_pct(base, 21)

def frac_468_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 105 fractal structure to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = close.diff().abs().rolling(70).sum()
    return _rank_pct(base, 63)

def frac_469_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 105 fractal structure to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = close.diff().abs().rolling(70).sum()
    return _rank_pct(base, 126)

def frac_470_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 105 fractal structure to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = close.diff().abs().rolling(70).sum()
    return _rank_pct(base, 252)

def frac_471_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 105 fractal structure distribution over 5d to detect tail risk or exhaustion.
    """
    base = close.diff().abs().rolling(70).sum()
    return _rolling_skew(base, 5)

def frac_472_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 105 fractal structure distribution over 21d to detect tail risk or exhaustion.
    """
    base = close.diff().abs().rolling(70).sum()
    return _rolling_skew(base, 21)

def frac_473_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 105 fractal structure distribution over 63d to detect tail risk or exhaustion.
    """
    base = close.diff().abs().rolling(70).sum()
    return _rolling_skew(base, 63)

def frac_474_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 105 fractal structure distribution over 126d to detect tail risk or exhaustion.
    """
    base = close.diff().abs().rolling(70).sum()
    return _rolling_skew(base, 126)

def frac_475_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 105 fractal structure distribution over 252d to detect tail risk or exhaustion.
    """
    base = close.diff().abs().rolling(70).sum()
    return _rolling_skew(base, 252)

def frac_476_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 105 fractal structure over 5d to capture explosive breakdown or reversal points.
    """
    base = close.diff().abs().rolling(70).sum()
    return _rolling_kurt(base, 5)

def frac_477_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 105 fractal structure over 21d to capture explosive breakdown or reversal points.
    """
    base = close.diff().abs().rolling(70).sum()
    return _rolling_kurt(base, 21)

def frac_478_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 105 fractal structure over 63d to capture explosive breakdown or reversal points.
    """
    base = close.diff().abs().rolling(70).sum()
    return _rolling_kurt(base, 63)

def frac_479_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 105 fractal structure over 126d to capture explosive breakdown or reversal points.
    """
    base = close.diff().abs().rolling(70).sum()
    return _rolling_kurt(base, 126)

def frac_480_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 105 fractal structure over 252d to capture explosive breakdown or reversal points.
    """
    base = close.diff().abs().rolling(70).sum()
    return _rolling_kurt(base, 252)

def frac_481_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 105 fractal structure for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = close.diff().abs().rolling(70).sum()
    return _safe_div(base, _rolling_std(base, 5))

def frac_482_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 105 fractal structure for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = close.diff().abs().rolling(70).sum()
    return _safe_div(base, _rolling_std(base, 21))

def frac_483_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 105 fractal structure for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = close.diff().abs().rolling(70).sum()
    return _safe_div(base, _rolling_std(base, 63))

def frac_484_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 105 fractal structure for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = close.diff().abs().rolling(70).sum()
    return _safe_div(base, _rolling_std(base, 126))

def frac_485_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 105 fractal structure for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = close.diff().abs().rolling(70).sum()
    return _safe_div(base, _rolling_std(base, 252))

def frac_486_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 105 fractal structure over 5d to stabilize variance and capture exponential shifts.
    """
    base = close.diff().abs().rolling(70).sum()
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def frac_487_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 105 fractal structure over 21d to stabilize variance and capture exponential shifts.
    """
    base = close.diff().abs().rolling(70).sum()
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def frac_488_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 105 fractal structure over 63d to stabilize variance and capture exponential shifts.
    """
    base = close.diff().abs().rolling(70).sum()
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def frac_489_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 105 fractal structure over 126d to stabilize variance and capture exponential shifts.
    """
    base = close.diff().abs().rolling(70).sum()
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def frac_490_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 105 fractal structure over 252d to stabilize variance and capture exponential shifts.
    """
    base = close.diff().abs().rolling(70).sum()
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def frac_491_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 105 fractal structure over a 5d horizon to identify extreme regimes.
    """
    base = close.diff().abs().rolling(75).sum()
    return _rolling_mean(base, 5)

def frac_492_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 105 fractal structure over a 21d horizon to identify extreme regimes.
    """
    base = close.diff().abs().rolling(75).sum()
    return _rolling_mean(base, 21)

def frac_493_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 105 fractal structure over a 63d horizon to identify extreme regimes.
    """
    base = close.diff().abs().rolling(75).sum()
    return _rolling_mean(base, 63)

def frac_494_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 105 fractal structure over a 126d horizon to identify extreme regimes.
    """
    base = close.diff().abs().rolling(75).sum()
    return _rolling_mean(base, 126)

def frac_495_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 105 fractal structure over a 252d horizon to identify extreme regimes.
    """
    base = close.diff().abs().rolling(75).sum()
    return _rolling_mean(base, 252)

def frac_496_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 105 fractal structure by measuring deviations from the 5d mean.
    """
    base = close.diff().abs().rolling(75).sum()
    return _zscore_rolling(base, 5)

def frac_497_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 105 fractal structure by measuring deviations from the 21d mean.
    """
    base = close.diff().abs().rolling(75).sum()
    return _zscore_rolling(base, 21)

def frac_498_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 105 fractal structure by measuring deviations from the 63d mean.
    """
    base = close.diff().abs().rolling(75).sum()
    return _zscore_rolling(base, 63)

def frac_499_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 105 fractal structure by measuring deviations from the 126d mean.
    """
    base = close.diff().abs().rolling(75).sum()
    return _zscore_rolling(base, 126)

def frac_500_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 105 fractal structure by measuring deviations from the 252d mean.
    """
    base = close.diff().abs().rolling(75).sum()
    return _zscore_rolling(base, 252)

def frac_501_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 105 fractal structure to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = close.diff().abs().rolling(75).sum()
    return _rank_pct(base, 5)

def frac_502_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 105 fractal structure to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = close.diff().abs().rolling(75).sum()
    return _rank_pct(base, 21)

def frac_503_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 105 fractal structure to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = close.diff().abs().rolling(75).sum()
    return _rank_pct(base, 63)

def frac_504_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 105 fractal structure to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = close.diff().abs().rolling(75).sum()
    return _rank_pct(base, 126)

def frac_505_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 105 fractal structure to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = close.diff().abs().rolling(75).sum()
    return _rank_pct(base, 252)

def frac_506_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 105 fractal structure distribution over 5d to detect tail risk or exhaustion.
    """
    base = close.diff().abs().rolling(75).sum()
    return _rolling_skew(base, 5)

def frac_507_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 105 fractal structure distribution over 21d to detect tail risk or exhaustion.
    """
    base = close.diff().abs().rolling(75).sum()
    return _rolling_skew(base, 21)

def frac_508_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 105 fractal structure distribution over 63d to detect tail risk or exhaustion.
    """
    base = close.diff().abs().rolling(75).sum()
    return _rolling_skew(base, 63)

def frac_509_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 105 fractal structure distribution over 126d to detect tail risk or exhaustion.
    """
    base = close.diff().abs().rolling(75).sum()
    return _rolling_skew(base, 126)

def frac_510_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 105 fractal structure distribution over 252d to detect tail risk or exhaustion.
    """
    base = close.diff().abs().rolling(75).sum()
    return _rolling_skew(base, 252)

def frac_511_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 105 fractal structure over 5d to capture explosive breakdown or reversal points.
    """
    base = close.diff().abs().rolling(75).sum()
    return _rolling_kurt(base, 5)

def frac_512_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 105 fractal structure over 21d to capture explosive breakdown or reversal points.
    """
    base = close.diff().abs().rolling(75).sum()
    return _rolling_kurt(base, 21)

def frac_513_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 105 fractal structure over 63d to capture explosive breakdown or reversal points.
    """
    base = close.diff().abs().rolling(75).sum()
    return _rolling_kurt(base, 63)

def frac_514_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 105 fractal structure over 126d to capture explosive breakdown or reversal points.
    """
    base = close.diff().abs().rolling(75).sum()
    return _rolling_kurt(base, 126)

def frac_515_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 105 fractal structure over 252d to capture explosive breakdown or reversal points.
    """
    base = close.diff().abs().rolling(75).sum()
    return _rolling_kurt(base, 252)

def frac_516_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 105 fractal structure for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = close.diff().abs().rolling(75).sum()
    return _safe_div(base, _rolling_std(base, 5))

def frac_517_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 105 fractal structure for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = close.diff().abs().rolling(75).sum()
    return _safe_div(base, _rolling_std(base, 21))

def frac_518_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 105 fractal structure for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = close.diff().abs().rolling(75).sum()
    return _safe_div(base, _rolling_std(base, 63))

def frac_519_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 105 fractal structure for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = close.diff().abs().rolling(75).sum()
    return _safe_div(base, _rolling_std(base, 126))

def frac_520_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 105 fractal structure for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = close.diff().abs().rolling(75).sum()
    return _safe_div(base, _rolling_std(base, 252))

def frac_521_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 105 fractal structure over 5d to stabilize variance and capture exponential shifts.
    """
    base = close.diff().abs().rolling(75).sum()
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def frac_522_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 105 fractal structure over 21d to stabilize variance and capture exponential shifts.
    """
    base = close.diff().abs().rolling(75).sum()
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def frac_523_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 105 fractal structure over 63d to stabilize variance and capture exponential shifts.
    """
    base = close.diff().abs().rolling(75).sum()
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def frac_524_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 105 fractal structure over 126d to stabilize variance and capture exponential shifts.
    """
    base = close.diff().abs().rolling(75).sum()
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def frac_525_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 105 fractal structure over 252d to stabilize variance and capture exponential shifts.
    """
    base = close.diff().abs().rolling(75).sum()
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))
