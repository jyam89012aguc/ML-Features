"""
108_108_drawdown_history_rank — Base Features 451-525
Domain: 108_drawdown_history_rank
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

def dhrk_451_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 108 drawdown history rank over 5d to stabilize variance and capture exponential shifts.
    """
    base = (close / close.rolling(260).max() - 1)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def dhrk_452_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 108 drawdown history rank over 21d to stabilize variance and capture exponential shifts.
    """
    base = (close / close.rolling(260).max() - 1)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def dhrk_453_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 108 drawdown history rank over 63d to stabilize variance and capture exponential shifts.
    """
    base = (close / close.rolling(260).max() - 1)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def dhrk_454_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 108 drawdown history rank over 126d to stabilize variance and capture exponential shifts.
    """
    base = (close / close.rolling(260).max() - 1)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def dhrk_455_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 108 drawdown history rank over 252d to stabilize variance and capture exponential shifts.
    """
    base = (close / close.rolling(260).max() - 1)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def dhrk_456_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 108 drawdown history rank over a 5d horizon to identify extreme regimes.
    """
    base = (close / close.rolling(280).max() - 1)
    return _rolling_mean(base, 5)

def dhrk_457_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 108 drawdown history rank over a 21d horizon to identify extreme regimes.
    """
    base = (close / close.rolling(280).max() - 1)
    return _rolling_mean(base, 21)

def dhrk_458_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 108 drawdown history rank over a 63d horizon to identify extreme regimes.
    """
    base = (close / close.rolling(280).max() - 1)
    return _rolling_mean(base, 63)

def dhrk_459_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 108 drawdown history rank over a 126d horizon to identify extreme regimes.
    """
    base = (close / close.rolling(280).max() - 1)
    return _rolling_mean(base, 126)

def dhrk_460_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 108 drawdown history rank over a 252d horizon to identify extreme regimes.
    """
    base = (close / close.rolling(280).max() - 1)
    return _rolling_mean(base, 252)

def dhrk_461_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 108 drawdown history rank by measuring deviations from the 5d mean.
    """
    base = (close / close.rolling(280).max() - 1)
    return _zscore_rolling(base, 5)

def dhrk_462_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 108 drawdown history rank by measuring deviations from the 21d mean.
    """
    base = (close / close.rolling(280).max() - 1)
    return _zscore_rolling(base, 21)

def dhrk_463_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 108 drawdown history rank by measuring deviations from the 63d mean.
    """
    base = (close / close.rolling(280).max() - 1)
    return _zscore_rolling(base, 63)

def dhrk_464_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 108 drawdown history rank by measuring deviations from the 126d mean.
    """
    base = (close / close.rolling(280).max() - 1)
    return _zscore_rolling(base, 126)

def dhrk_465_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 108 drawdown history rank by measuring deviations from the 252d mean.
    """
    base = (close / close.rolling(280).max() - 1)
    return _zscore_rolling(base, 252)

def dhrk_466_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 108 drawdown history rank to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = (close / close.rolling(280).max() - 1)
    return _rank_pct(base, 5)

def dhrk_467_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 108 drawdown history rank to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = (close / close.rolling(280).max() - 1)
    return _rank_pct(base, 21)

def dhrk_468_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 108 drawdown history rank to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = (close / close.rolling(280).max() - 1)
    return _rank_pct(base, 63)

def dhrk_469_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 108 drawdown history rank to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = (close / close.rolling(280).max() - 1)
    return _rank_pct(base, 126)

def dhrk_470_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 108 drawdown history rank to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = (close / close.rolling(280).max() - 1)
    return _rank_pct(base, 252)

def dhrk_471_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 108 drawdown history rank distribution over 5d to detect tail risk or exhaustion.
    """
    base = (close / close.rolling(280).max() - 1)
    return _rolling_skew(base, 5)

def dhrk_472_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 108 drawdown history rank distribution over 21d to detect tail risk or exhaustion.
    """
    base = (close / close.rolling(280).max() - 1)
    return _rolling_skew(base, 21)

def dhrk_473_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 108 drawdown history rank distribution over 63d to detect tail risk or exhaustion.
    """
    base = (close / close.rolling(280).max() - 1)
    return _rolling_skew(base, 63)

def dhrk_474_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 108 drawdown history rank distribution over 126d to detect tail risk or exhaustion.
    """
    base = (close / close.rolling(280).max() - 1)
    return _rolling_skew(base, 126)

def dhrk_475_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 108 drawdown history rank distribution over 252d to detect tail risk or exhaustion.
    """
    base = (close / close.rolling(280).max() - 1)
    return _rolling_skew(base, 252)

def dhrk_476_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 108 drawdown history rank over 5d to capture explosive breakdown or reversal points.
    """
    base = (close / close.rolling(280).max() - 1)
    return _rolling_kurt(base, 5)

def dhrk_477_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 108 drawdown history rank over 21d to capture explosive breakdown or reversal points.
    """
    base = (close / close.rolling(280).max() - 1)
    return _rolling_kurt(base, 21)

def dhrk_478_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 108 drawdown history rank over 63d to capture explosive breakdown or reversal points.
    """
    base = (close / close.rolling(280).max() - 1)
    return _rolling_kurt(base, 63)

def dhrk_479_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 108 drawdown history rank over 126d to capture explosive breakdown or reversal points.
    """
    base = (close / close.rolling(280).max() - 1)
    return _rolling_kurt(base, 126)

def dhrk_480_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 108 drawdown history rank over 252d to capture explosive breakdown or reversal points.
    """
    base = (close / close.rolling(280).max() - 1)
    return _rolling_kurt(base, 252)

def dhrk_481_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 108 drawdown history rank for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = (close / close.rolling(280).max() - 1)
    return _safe_div(base, _rolling_std(base, 5))

def dhrk_482_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 108 drawdown history rank for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = (close / close.rolling(280).max() - 1)
    return _safe_div(base, _rolling_std(base, 21))

def dhrk_483_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 108 drawdown history rank for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = (close / close.rolling(280).max() - 1)
    return _safe_div(base, _rolling_std(base, 63))

def dhrk_484_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 108 drawdown history rank for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = (close / close.rolling(280).max() - 1)
    return _safe_div(base, _rolling_std(base, 126))

def dhrk_485_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 108 drawdown history rank for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = (close / close.rolling(280).max() - 1)
    return _safe_div(base, _rolling_std(base, 252))

def dhrk_486_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 108 drawdown history rank over 5d to stabilize variance and capture exponential shifts.
    """
    base = (close / close.rolling(280).max() - 1)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def dhrk_487_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 108 drawdown history rank over 21d to stabilize variance and capture exponential shifts.
    """
    base = (close / close.rolling(280).max() - 1)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def dhrk_488_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 108 drawdown history rank over 63d to stabilize variance and capture exponential shifts.
    """
    base = (close / close.rolling(280).max() - 1)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def dhrk_489_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 108 drawdown history rank over 126d to stabilize variance and capture exponential shifts.
    """
    base = (close / close.rolling(280).max() - 1)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def dhrk_490_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 108 drawdown history rank over 252d to stabilize variance and capture exponential shifts.
    """
    base = (close / close.rolling(280).max() - 1)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def dhrk_491_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 108 drawdown history rank over a 5d horizon to identify extreme regimes.
    """
    base = (close / close.rolling(300).max() - 1)
    return _rolling_mean(base, 5)

def dhrk_492_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 108 drawdown history rank over a 21d horizon to identify extreme regimes.
    """
    base = (close / close.rolling(300).max() - 1)
    return _rolling_mean(base, 21)

def dhrk_493_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 108 drawdown history rank over a 63d horizon to identify extreme regimes.
    """
    base = (close / close.rolling(300).max() - 1)
    return _rolling_mean(base, 63)

def dhrk_494_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 108 drawdown history rank over a 126d horizon to identify extreme regimes.
    """
    base = (close / close.rolling(300).max() - 1)
    return _rolling_mean(base, 126)

def dhrk_495_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 108 drawdown history rank over a 252d horizon to identify extreme regimes.
    """
    base = (close / close.rolling(300).max() - 1)
    return _rolling_mean(base, 252)

def dhrk_496_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 108 drawdown history rank by measuring deviations from the 5d mean.
    """
    base = (close / close.rolling(300).max() - 1)
    return _zscore_rolling(base, 5)

def dhrk_497_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 108 drawdown history rank by measuring deviations from the 21d mean.
    """
    base = (close / close.rolling(300).max() - 1)
    return _zscore_rolling(base, 21)

def dhrk_498_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 108 drawdown history rank by measuring deviations from the 63d mean.
    """
    base = (close / close.rolling(300).max() - 1)
    return _zscore_rolling(base, 63)

def dhrk_499_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 108 drawdown history rank by measuring deviations from the 126d mean.
    """
    base = (close / close.rolling(300).max() - 1)
    return _zscore_rolling(base, 126)

def dhrk_500_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 108 drawdown history rank by measuring deviations from the 252d mean.
    """
    base = (close / close.rolling(300).max() - 1)
    return _zscore_rolling(base, 252)

def dhrk_501_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 108 drawdown history rank to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = (close / close.rolling(300).max() - 1)
    return _rank_pct(base, 5)

def dhrk_502_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 108 drawdown history rank to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = (close / close.rolling(300).max() - 1)
    return _rank_pct(base, 21)

def dhrk_503_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 108 drawdown history rank to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = (close / close.rolling(300).max() - 1)
    return _rank_pct(base, 63)

def dhrk_504_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 108 drawdown history rank to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = (close / close.rolling(300).max() - 1)
    return _rank_pct(base, 126)

def dhrk_505_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 108 drawdown history rank to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = (close / close.rolling(300).max() - 1)
    return _rank_pct(base, 252)

def dhrk_506_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 108 drawdown history rank distribution over 5d to detect tail risk or exhaustion.
    """
    base = (close / close.rolling(300).max() - 1)
    return _rolling_skew(base, 5)

def dhrk_507_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 108 drawdown history rank distribution over 21d to detect tail risk or exhaustion.
    """
    base = (close / close.rolling(300).max() - 1)
    return _rolling_skew(base, 21)

def dhrk_508_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 108 drawdown history rank distribution over 63d to detect tail risk or exhaustion.
    """
    base = (close / close.rolling(300).max() - 1)
    return _rolling_skew(base, 63)

def dhrk_509_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 108 drawdown history rank distribution over 126d to detect tail risk or exhaustion.
    """
    base = (close / close.rolling(300).max() - 1)
    return _rolling_skew(base, 126)

def dhrk_510_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 108 drawdown history rank distribution over 252d to detect tail risk or exhaustion.
    """
    base = (close / close.rolling(300).max() - 1)
    return _rolling_skew(base, 252)

def dhrk_511_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 108 drawdown history rank over 5d to capture explosive breakdown or reversal points.
    """
    base = (close / close.rolling(300).max() - 1)
    return _rolling_kurt(base, 5)

def dhrk_512_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 108 drawdown history rank over 21d to capture explosive breakdown or reversal points.
    """
    base = (close / close.rolling(300).max() - 1)
    return _rolling_kurt(base, 21)

def dhrk_513_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 108 drawdown history rank over 63d to capture explosive breakdown or reversal points.
    """
    base = (close / close.rolling(300).max() - 1)
    return _rolling_kurt(base, 63)

def dhrk_514_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 108 drawdown history rank over 126d to capture explosive breakdown or reversal points.
    """
    base = (close / close.rolling(300).max() - 1)
    return _rolling_kurt(base, 126)

def dhrk_515_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 108 drawdown history rank over 252d to capture explosive breakdown or reversal points.
    """
    base = (close / close.rolling(300).max() - 1)
    return _rolling_kurt(base, 252)

def dhrk_516_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 108 drawdown history rank for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = (close / close.rolling(300).max() - 1)
    return _safe_div(base, _rolling_std(base, 5))

def dhrk_517_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 108 drawdown history rank for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = (close / close.rolling(300).max() - 1)
    return _safe_div(base, _rolling_std(base, 21))

def dhrk_518_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 108 drawdown history rank for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = (close / close.rolling(300).max() - 1)
    return _safe_div(base, _rolling_std(base, 63))

def dhrk_519_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 108 drawdown history rank for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = (close / close.rolling(300).max() - 1)
    return _safe_div(base, _rolling_std(base, 126))

def dhrk_520_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 108 drawdown history rank for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = (close / close.rolling(300).max() - 1)
    return _safe_div(base, _rolling_std(base, 252))

def dhrk_521_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 108 drawdown history rank over 5d to stabilize variance and capture exponential shifts.
    """
    base = (close / close.rolling(300).max() - 1)
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def dhrk_522_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 108 drawdown history rank over 21d to stabilize variance and capture exponential shifts.
    """
    base = (close / close.rolling(300).max() - 1)
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def dhrk_523_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 108 drawdown history rank over 63d to stabilize variance and capture exponential shifts.
    """
    base = (close / close.rolling(300).max() - 1)
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def dhrk_524_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 108 drawdown history rank over 126d to stabilize variance and capture exponential shifts.
    """
    base = (close / close.rolling(300).max() - 1)
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def dhrk_525_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 108 drawdown history rank over 252d to stabilize variance and capture exponential shifts.
    """
    base = (close / close.rolling(300).max() - 1)
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))
