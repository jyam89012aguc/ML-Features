"""
04_04_drawdown_velocity — Base Features 451-525
Domain: 04_drawdown_velocity
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

def dvel_451_lognorm_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 04 drawdown velocity over 5d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(13).rolling(65).mean())
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def dvel_452_lognorm_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 04 drawdown velocity over 21d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(13).rolling(65).mean())
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def dvel_453_lognorm_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 04 drawdown velocity over 63d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(13).rolling(65).mean())
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def dvel_454_lognorm_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 04 drawdown velocity over 126d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(13).rolling(65).mean())
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def dvel_455_lognorm_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 04 drawdown velocity over 252d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(13).rolling(65).mean())
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def dvel_456_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 04 drawdown velocity over a 5d horizon to identify extreme regimes.
    """
    base = (close.pct_change(14).rolling(70).mean())
    return _rolling_mean(base, 5)

def dvel_457_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 04 drawdown velocity over a 21d horizon to identify extreme regimes.
    """
    base = (close.pct_change(14).rolling(70).mean())
    return _rolling_mean(base, 21)

def dvel_458_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 04 drawdown velocity over a 63d horizon to identify extreme regimes.
    """
    base = (close.pct_change(14).rolling(70).mean())
    return _rolling_mean(base, 63)

def dvel_459_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 04 drawdown velocity over a 126d horizon to identify extreme regimes.
    """
    base = (close.pct_change(14).rolling(70).mean())
    return _rolling_mean(base, 126)

def dvel_460_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 04 drawdown velocity over a 252d horizon to identify extreme regimes.
    """
    base = (close.pct_change(14).rolling(70).mean())
    return _rolling_mean(base, 252)

def dvel_461_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 04 drawdown velocity by measuring deviations from the 5d mean.
    """
    base = (close.pct_change(14).rolling(70).mean())
    return _zscore_rolling(base, 5)

def dvel_462_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 04 drawdown velocity by measuring deviations from the 21d mean.
    """
    base = (close.pct_change(14).rolling(70).mean())
    return _zscore_rolling(base, 21)

def dvel_463_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 04 drawdown velocity by measuring deviations from the 63d mean.
    """
    base = (close.pct_change(14).rolling(70).mean())
    return _zscore_rolling(base, 63)

def dvel_464_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 04 drawdown velocity by measuring deviations from the 126d mean.
    """
    base = (close.pct_change(14).rolling(70).mean())
    return _zscore_rolling(base, 126)

def dvel_465_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 04 drawdown velocity by measuring deviations from the 252d mean.
    """
    base = (close.pct_change(14).rolling(70).mean())
    return _zscore_rolling(base, 252)

def dvel_466_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 04 drawdown velocity to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = (close.pct_change(14).rolling(70).mean())
    return _rank_pct(base, 5)

def dvel_467_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 04 drawdown velocity to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = (close.pct_change(14).rolling(70).mean())
    return _rank_pct(base, 21)

def dvel_468_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 04 drawdown velocity to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = (close.pct_change(14).rolling(70).mean())
    return _rank_pct(base, 63)

def dvel_469_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 04 drawdown velocity to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = (close.pct_change(14).rolling(70).mean())
    return _rank_pct(base, 126)

def dvel_470_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 04 drawdown velocity to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = (close.pct_change(14).rolling(70).mean())
    return _rank_pct(base, 252)

def dvel_471_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 04 drawdown velocity distribution over 5d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(14).rolling(70).mean())
    return _rolling_skew(base, 5)

def dvel_472_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 04 drawdown velocity distribution over 21d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(14).rolling(70).mean())
    return _rolling_skew(base, 21)

def dvel_473_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 04 drawdown velocity distribution over 63d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(14).rolling(70).mean())
    return _rolling_skew(base, 63)

def dvel_474_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 04 drawdown velocity distribution over 126d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(14).rolling(70).mean())
    return _rolling_skew(base, 126)

def dvel_475_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 04 drawdown velocity distribution over 252d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(14).rolling(70).mean())
    return _rolling_skew(base, 252)

def dvel_476_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 04 drawdown velocity over 5d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(14).rolling(70).mean())
    return _rolling_kurt(base, 5)

def dvel_477_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 04 drawdown velocity over 21d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(14).rolling(70).mean())
    return _rolling_kurt(base, 21)

def dvel_478_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 04 drawdown velocity over 63d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(14).rolling(70).mean())
    return _rolling_kurt(base, 63)

def dvel_479_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 04 drawdown velocity over 126d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(14).rolling(70).mean())
    return _rolling_kurt(base, 126)

def dvel_480_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 04 drawdown velocity over 252d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(14).rolling(70).mean())
    return _rolling_kurt(base, 252)

def dvel_481_voladj_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 04 drawdown velocity for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(14).rolling(70).mean())
    return _safe_div(base, _rolling_std(base, 5))

def dvel_482_voladj_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 04 drawdown velocity for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(14).rolling(70).mean())
    return _safe_div(base, _rolling_std(base, 21))

def dvel_483_voladj_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 04 drawdown velocity for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(14).rolling(70).mean())
    return _safe_div(base, _rolling_std(base, 63))

def dvel_484_voladj_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 04 drawdown velocity for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(14).rolling(70).mean())
    return _safe_div(base, _rolling_std(base, 126))

def dvel_485_voladj_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 04 drawdown velocity for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(14).rolling(70).mean())
    return _safe_div(base, _rolling_std(base, 252))

def dvel_486_lognorm_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 04 drawdown velocity over 5d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(14).rolling(70).mean())
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def dvel_487_lognorm_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 04 drawdown velocity over 21d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(14).rolling(70).mean())
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def dvel_488_lognorm_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 04 drawdown velocity over 63d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(14).rolling(70).mean())
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def dvel_489_lognorm_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 04 drawdown velocity over 126d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(14).rolling(70).mean())
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def dvel_490_lognorm_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 04 drawdown velocity over 252d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(14).rolling(70).mean())
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def dvel_491_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 04 drawdown velocity over a 5d horizon to identify extreme regimes.
    """
    base = (close.pct_change(15).rolling(75).mean())
    return _rolling_mean(base, 5)

def dvel_492_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 04 drawdown velocity over a 21d horizon to identify extreme regimes.
    """
    base = (close.pct_change(15).rolling(75).mean())
    return _rolling_mean(base, 21)

def dvel_493_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 04 drawdown velocity over a 63d horizon to identify extreme regimes.
    """
    base = (close.pct_change(15).rolling(75).mean())
    return _rolling_mean(base, 63)

def dvel_494_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 04 drawdown velocity over a 126d horizon to identify extreme regimes.
    """
    base = (close.pct_change(15).rolling(75).mean())
    return _rolling_mean(base, 126)

def dvel_495_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 04 drawdown velocity over a 252d horizon to identify extreme regimes.
    """
    base = (close.pct_change(15).rolling(75).mean())
    return _rolling_mean(base, 252)

def dvel_496_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 04 drawdown velocity by measuring deviations from the 5d mean.
    """
    base = (close.pct_change(15).rolling(75).mean())
    return _zscore_rolling(base, 5)

def dvel_497_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 04 drawdown velocity by measuring deviations from the 21d mean.
    """
    base = (close.pct_change(15).rolling(75).mean())
    return _zscore_rolling(base, 21)

def dvel_498_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 04 drawdown velocity by measuring deviations from the 63d mean.
    """
    base = (close.pct_change(15).rolling(75).mean())
    return _zscore_rolling(base, 63)

def dvel_499_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 04 drawdown velocity by measuring deviations from the 126d mean.
    """
    base = (close.pct_change(15).rolling(75).mean())
    return _zscore_rolling(base, 126)

def dvel_500_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 04 drawdown velocity by measuring deviations from the 252d mean.
    """
    base = (close.pct_change(15).rolling(75).mean())
    return _zscore_rolling(base, 252)

def dvel_501_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 04 drawdown velocity to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = (close.pct_change(15).rolling(75).mean())
    return _rank_pct(base, 5)

def dvel_502_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 04 drawdown velocity to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = (close.pct_change(15).rolling(75).mean())
    return _rank_pct(base, 21)

def dvel_503_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 04 drawdown velocity to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = (close.pct_change(15).rolling(75).mean())
    return _rank_pct(base, 63)

def dvel_504_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 04 drawdown velocity to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = (close.pct_change(15).rolling(75).mean())
    return _rank_pct(base, 126)

def dvel_505_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 04 drawdown velocity to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = (close.pct_change(15).rolling(75).mean())
    return _rank_pct(base, 252)

def dvel_506_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 04 drawdown velocity distribution over 5d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(15).rolling(75).mean())
    return _rolling_skew(base, 5)

def dvel_507_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 04 drawdown velocity distribution over 21d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(15).rolling(75).mean())
    return _rolling_skew(base, 21)

def dvel_508_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 04 drawdown velocity distribution over 63d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(15).rolling(75).mean())
    return _rolling_skew(base, 63)

def dvel_509_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 04 drawdown velocity distribution over 126d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(15).rolling(75).mean())
    return _rolling_skew(base, 126)

def dvel_510_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 04 drawdown velocity distribution over 252d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(15).rolling(75).mean())
    return _rolling_skew(base, 252)

def dvel_511_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 04 drawdown velocity over 5d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(15).rolling(75).mean())
    return _rolling_kurt(base, 5)

def dvel_512_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 04 drawdown velocity over 21d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(15).rolling(75).mean())
    return _rolling_kurt(base, 21)

def dvel_513_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 04 drawdown velocity over 63d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(15).rolling(75).mean())
    return _rolling_kurt(base, 63)

def dvel_514_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 04 drawdown velocity over 126d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(15).rolling(75).mean())
    return _rolling_kurt(base, 126)

def dvel_515_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 04 drawdown velocity over 252d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(15).rolling(75).mean())
    return _rolling_kurt(base, 252)

def dvel_516_voladj_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 04 drawdown velocity for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(15).rolling(75).mean())
    return _safe_div(base, _rolling_std(base, 5))

def dvel_517_voladj_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 04 drawdown velocity for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(15).rolling(75).mean())
    return _safe_div(base, _rolling_std(base, 21))

def dvel_518_voladj_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 04 drawdown velocity for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(15).rolling(75).mean())
    return _safe_div(base, _rolling_std(base, 63))

def dvel_519_voladj_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 04 drawdown velocity for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(15).rolling(75).mean())
    return _safe_div(base, _rolling_std(base, 126))

def dvel_520_voladj_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 04 drawdown velocity for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(15).rolling(75).mean())
    return _safe_div(base, _rolling_std(base, 252))

def dvel_521_lognorm_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 04 drawdown velocity over 5d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(15).rolling(75).mean())
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def dvel_522_lognorm_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 04 drawdown velocity over 21d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(15).rolling(75).mean())
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def dvel_523_lognorm_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 04 drawdown velocity over 63d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(15).rolling(75).mean())
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def dvel_524_lognorm_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 04 drawdown velocity over 126d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(15).rolling(75).mean())
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def dvel_525_lognorm_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 04 drawdown velocity over 252d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(15).rolling(75).mean())
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))
