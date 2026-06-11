"""
106_106_support_violation — Base Features 451-525
Domain: 106_support_violation
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

def supv_451_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 106 support violation over 5d to stabilize variance and capture exponential shifts.
    """
    base = close / low.rolling(130).min() - 1
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def supv_452_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 106 support violation over 21d to stabilize variance and capture exponential shifts.
    """
    base = close / low.rolling(130).min() - 1
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def supv_453_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 106 support violation over 63d to stabilize variance and capture exponential shifts.
    """
    base = close / low.rolling(130).min() - 1
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def supv_454_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 106 support violation over 126d to stabilize variance and capture exponential shifts.
    """
    base = close / low.rolling(130).min() - 1
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def supv_455_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 106 support violation over 252d to stabilize variance and capture exponential shifts.
    """
    base = close / low.rolling(130).min() - 1
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def supv_456_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 106 support violation over a 5d horizon to identify extreme regimes.
    """
    base = close / low.rolling(140).min() - 1
    return _rolling_mean(base, 5)

def supv_457_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 106 support violation over a 21d horizon to identify extreme regimes.
    """
    base = close / low.rolling(140).min() - 1
    return _rolling_mean(base, 21)

def supv_458_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 106 support violation over a 63d horizon to identify extreme regimes.
    """
    base = close / low.rolling(140).min() - 1
    return _rolling_mean(base, 63)

def supv_459_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 106 support violation over a 126d horizon to identify extreme regimes.
    """
    base = close / low.rolling(140).min() - 1
    return _rolling_mean(base, 126)

def supv_460_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 106 support violation over a 252d horizon to identify extreme regimes.
    """
    base = close / low.rolling(140).min() - 1
    return _rolling_mean(base, 252)

def supv_461_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 106 support violation by measuring deviations from the 5d mean.
    """
    base = close / low.rolling(140).min() - 1
    return _zscore_rolling(base, 5)

def supv_462_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 106 support violation by measuring deviations from the 21d mean.
    """
    base = close / low.rolling(140).min() - 1
    return _zscore_rolling(base, 21)

def supv_463_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 106 support violation by measuring deviations from the 63d mean.
    """
    base = close / low.rolling(140).min() - 1
    return _zscore_rolling(base, 63)

def supv_464_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 106 support violation by measuring deviations from the 126d mean.
    """
    base = close / low.rolling(140).min() - 1
    return _zscore_rolling(base, 126)

def supv_465_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 106 support violation by measuring deviations from the 252d mean.
    """
    base = close / low.rolling(140).min() - 1
    return _zscore_rolling(base, 252)

def supv_466_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 106 support violation to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = close / low.rolling(140).min() - 1
    return _rank_pct(base, 5)

def supv_467_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 106 support violation to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = close / low.rolling(140).min() - 1
    return _rank_pct(base, 21)

def supv_468_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 106 support violation to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = close / low.rolling(140).min() - 1
    return _rank_pct(base, 63)

def supv_469_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 106 support violation to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = close / low.rolling(140).min() - 1
    return _rank_pct(base, 126)

def supv_470_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 106 support violation to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = close / low.rolling(140).min() - 1
    return _rank_pct(base, 252)

def supv_471_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 106 support violation distribution over 5d to detect tail risk or exhaustion.
    """
    base = close / low.rolling(140).min() - 1
    return _rolling_skew(base, 5)

def supv_472_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 106 support violation distribution over 21d to detect tail risk or exhaustion.
    """
    base = close / low.rolling(140).min() - 1
    return _rolling_skew(base, 21)

def supv_473_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 106 support violation distribution over 63d to detect tail risk or exhaustion.
    """
    base = close / low.rolling(140).min() - 1
    return _rolling_skew(base, 63)

def supv_474_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 106 support violation distribution over 126d to detect tail risk or exhaustion.
    """
    base = close / low.rolling(140).min() - 1
    return _rolling_skew(base, 126)

def supv_475_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 106 support violation distribution over 252d to detect tail risk or exhaustion.
    """
    base = close / low.rolling(140).min() - 1
    return _rolling_skew(base, 252)

def supv_476_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 106 support violation over 5d to capture explosive breakdown or reversal points.
    """
    base = close / low.rolling(140).min() - 1
    return _rolling_kurt(base, 5)

def supv_477_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 106 support violation over 21d to capture explosive breakdown or reversal points.
    """
    base = close / low.rolling(140).min() - 1
    return _rolling_kurt(base, 21)

def supv_478_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 106 support violation over 63d to capture explosive breakdown or reversal points.
    """
    base = close / low.rolling(140).min() - 1
    return _rolling_kurt(base, 63)

def supv_479_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 106 support violation over 126d to capture explosive breakdown or reversal points.
    """
    base = close / low.rolling(140).min() - 1
    return _rolling_kurt(base, 126)

def supv_480_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 106 support violation over 252d to capture explosive breakdown or reversal points.
    """
    base = close / low.rolling(140).min() - 1
    return _rolling_kurt(base, 252)

def supv_481_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 106 support violation for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = close / low.rolling(140).min() - 1
    return _safe_div(base, _rolling_std(base, 5))

def supv_482_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 106 support violation for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = close / low.rolling(140).min() - 1
    return _safe_div(base, _rolling_std(base, 21))

def supv_483_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 106 support violation for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = close / low.rolling(140).min() - 1
    return _safe_div(base, _rolling_std(base, 63))

def supv_484_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 106 support violation for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = close / low.rolling(140).min() - 1
    return _safe_div(base, _rolling_std(base, 126))

def supv_485_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 106 support violation for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = close / low.rolling(140).min() - 1
    return _safe_div(base, _rolling_std(base, 252))

def supv_486_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 106 support violation over 5d to stabilize variance and capture exponential shifts.
    """
    base = close / low.rolling(140).min() - 1
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def supv_487_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 106 support violation over 21d to stabilize variance and capture exponential shifts.
    """
    base = close / low.rolling(140).min() - 1
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def supv_488_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 106 support violation over 63d to stabilize variance and capture exponential shifts.
    """
    base = close / low.rolling(140).min() - 1
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def supv_489_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 106 support violation over 126d to stabilize variance and capture exponential shifts.
    """
    base = close / low.rolling(140).min() - 1
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def supv_490_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 106 support violation over 252d to stabilize variance and capture exponential shifts.
    """
    base = close / low.rolling(140).min() - 1
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def supv_491_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 106 support violation over a 5d horizon to identify extreme regimes.
    """
    base = close / low.rolling(150).min() - 1
    return _rolling_mean(base, 5)

def supv_492_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 106 support violation over a 21d horizon to identify extreme regimes.
    """
    base = close / low.rolling(150).min() - 1
    return _rolling_mean(base, 21)

def supv_493_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 106 support violation over a 63d horizon to identify extreme regimes.
    """
    base = close / low.rolling(150).min() - 1
    return _rolling_mean(base, 63)

def supv_494_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 106 support violation over a 126d horizon to identify extreme regimes.
    """
    base = close / low.rolling(150).min() - 1
    return _rolling_mean(base, 126)

def supv_495_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 106 support violation over a 252d horizon to identify extreme regimes.
    """
    base = close / low.rolling(150).min() - 1
    return _rolling_mean(base, 252)

def supv_496_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 106 support violation by measuring deviations from the 5d mean.
    """
    base = close / low.rolling(150).min() - 1
    return _zscore_rolling(base, 5)

def supv_497_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 106 support violation by measuring deviations from the 21d mean.
    """
    base = close / low.rolling(150).min() - 1
    return _zscore_rolling(base, 21)

def supv_498_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 106 support violation by measuring deviations from the 63d mean.
    """
    base = close / low.rolling(150).min() - 1
    return _zscore_rolling(base, 63)

def supv_499_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 106 support violation by measuring deviations from the 126d mean.
    """
    base = close / low.rolling(150).min() - 1
    return _zscore_rolling(base, 126)

def supv_500_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 106 support violation by measuring deviations from the 252d mean.
    """
    base = close / low.rolling(150).min() - 1
    return _zscore_rolling(base, 252)

def supv_501_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 106 support violation to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = close / low.rolling(150).min() - 1
    return _rank_pct(base, 5)

def supv_502_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 106 support violation to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = close / low.rolling(150).min() - 1
    return _rank_pct(base, 21)

def supv_503_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 106 support violation to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = close / low.rolling(150).min() - 1
    return _rank_pct(base, 63)

def supv_504_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 106 support violation to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = close / low.rolling(150).min() - 1
    return _rank_pct(base, 126)

def supv_505_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 106 support violation to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = close / low.rolling(150).min() - 1
    return _rank_pct(base, 252)

def supv_506_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 106 support violation distribution over 5d to detect tail risk or exhaustion.
    """
    base = close / low.rolling(150).min() - 1
    return _rolling_skew(base, 5)

def supv_507_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 106 support violation distribution over 21d to detect tail risk or exhaustion.
    """
    base = close / low.rolling(150).min() - 1
    return _rolling_skew(base, 21)

def supv_508_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 106 support violation distribution over 63d to detect tail risk or exhaustion.
    """
    base = close / low.rolling(150).min() - 1
    return _rolling_skew(base, 63)

def supv_509_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 106 support violation distribution over 126d to detect tail risk or exhaustion.
    """
    base = close / low.rolling(150).min() - 1
    return _rolling_skew(base, 126)

def supv_510_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 106 support violation distribution over 252d to detect tail risk or exhaustion.
    """
    base = close / low.rolling(150).min() - 1
    return _rolling_skew(base, 252)

def supv_511_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 106 support violation over 5d to capture explosive breakdown or reversal points.
    """
    base = close / low.rolling(150).min() - 1
    return _rolling_kurt(base, 5)

def supv_512_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 106 support violation over 21d to capture explosive breakdown or reversal points.
    """
    base = close / low.rolling(150).min() - 1
    return _rolling_kurt(base, 21)

def supv_513_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 106 support violation over 63d to capture explosive breakdown or reversal points.
    """
    base = close / low.rolling(150).min() - 1
    return _rolling_kurt(base, 63)

def supv_514_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 106 support violation over 126d to capture explosive breakdown or reversal points.
    """
    base = close / low.rolling(150).min() - 1
    return _rolling_kurt(base, 126)

def supv_515_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 106 support violation over 252d to capture explosive breakdown or reversal points.
    """
    base = close / low.rolling(150).min() - 1
    return _rolling_kurt(base, 252)

def supv_516_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 106 support violation for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = close / low.rolling(150).min() - 1
    return _safe_div(base, _rolling_std(base, 5))

def supv_517_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 106 support violation for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = close / low.rolling(150).min() - 1
    return _safe_div(base, _rolling_std(base, 21))

def supv_518_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 106 support violation for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = close / low.rolling(150).min() - 1
    return _safe_div(base, _rolling_std(base, 63))

def supv_519_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 106 support violation for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = close / low.rolling(150).min() - 1
    return _safe_div(base, _rolling_std(base, 126))

def supv_520_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 106 support violation for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = close / low.rolling(150).min() - 1
    return _safe_div(base, _rolling_std(base, 252))

def supv_521_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 106 support violation over 5d to stabilize variance and capture exponential shifts.
    """
    base = close / low.rolling(150).min() - 1
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def supv_522_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 106 support violation over 21d to stabilize variance and capture exponential shifts.
    """
    base = close / low.rolling(150).min() - 1
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def supv_523_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 106 support violation over 63d to stabilize variance and capture exponential shifts.
    """
    base = close / low.rolling(150).min() - 1
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def supv_524_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 106 support violation over 126d to stabilize variance and capture exponential shifts.
    """
    base = close / low.rolling(150).min() - 1
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def supv_525_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 106 support violation over 252d to stabilize variance and capture exponential shifts.
    """
    base = close / low.rolling(150).min() - 1
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))
