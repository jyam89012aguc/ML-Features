"""
33_33_trend_breakdown — Base Features 451-525
Domain: 33_trend_breakdown
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

def tbrk_451_lognorm_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 33 trend breakdown over 5d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(13).rolling(65).mean())
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def tbrk_452_lognorm_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 33 trend breakdown over 21d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(13).rolling(65).mean())
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def tbrk_453_lognorm_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 33 trend breakdown over 63d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(13).rolling(65).mean())
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def tbrk_454_lognorm_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 33 trend breakdown over 126d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(13).rolling(65).mean())
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def tbrk_455_lognorm_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 33 trend breakdown over 252d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(13).rolling(65).mean())
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def tbrk_456_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 33 trend breakdown over a 5d horizon to identify extreme regimes.
    """
    base = (close.pct_change(14).rolling(70).mean())
    return _rolling_mean(base, 5)

def tbrk_457_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 33 trend breakdown over a 21d horizon to identify extreme regimes.
    """
    base = (close.pct_change(14).rolling(70).mean())
    return _rolling_mean(base, 21)

def tbrk_458_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 33 trend breakdown over a 63d horizon to identify extreme regimes.
    """
    base = (close.pct_change(14).rolling(70).mean())
    return _rolling_mean(base, 63)

def tbrk_459_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 33 trend breakdown over a 126d horizon to identify extreme regimes.
    """
    base = (close.pct_change(14).rolling(70).mean())
    return _rolling_mean(base, 126)

def tbrk_460_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 33 trend breakdown over a 252d horizon to identify extreme regimes.
    """
    base = (close.pct_change(14).rolling(70).mean())
    return _rolling_mean(base, 252)

def tbrk_461_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 33 trend breakdown by measuring deviations from the 5d mean.
    """
    base = (close.pct_change(14).rolling(70).mean())
    return _zscore_rolling(base, 5)

def tbrk_462_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 33 trend breakdown by measuring deviations from the 21d mean.
    """
    base = (close.pct_change(14).rolling(70).mean())
    return _zscore_rolling(base, 21)

def tbrk_463_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 33 trend breakdown by measuring deviations from the 63d mean.
    """
    base = (close.pct_change(14).rolling(70).mean())
    return _zscore_rolling(base, 63)

def tbrk_464_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 33 trend breakdown by measuring deviations from the 126d mean.
    """
    base = (close.pct_change(14).rolling(70).mean())
    return _zscore_rolling(base, 126)

def tbrk_465_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 33 trend breakdown by measuring deviations from the 252d mean.
    """
    base = (close.pct_change(14).rolling(70).mean())
    return _zscore_rolling(base, 252)

def tbrk_466_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 33 trend breakdown to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = (close.pct_change(14).rolling(70).mean())
    return _rank_pct(base, 5)

def tbrk_467_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 33 trend breakdown to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = (close.pct_change(14).rolling(70).mean())
    return _rank_pct(base, 21)

def tbrk_468_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 33 trend breakdown to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = (close.pct_change(14).rolling(70).mean())
    return _rank_pct(base, 63)

def tbrk_469_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 33 trend breakdown to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = (close.pct_change(14).rolling(70).mean())
    return _rank_pct(base, 126)

def tbrk_470_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 33 trend breakdown to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = (close.pct_change(14).rolling(70).mean())
    return _rank_pct(base, 252)

def tbrk_471_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 33 trend breakdown distribution over 5d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(14).rolling(70).mean())
    return _rolling_skew(base, 5)

def tbrk_472_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 33 trend breakdown distribution over 21d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(14).rolling(70).mean())
    return _rolling_skew(base, 21)

def tbrk_473_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 33 trend breakdown distribution over 63d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(14).rolling(70).mean())
    return _rolling_skew(base, 63)

def tbrk_474_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 33 trend breakdown distribution over 126d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(14).rolling(70).mean())
    return _rolling_skew(base, 126)

def tbrk_475_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 33 trend breakdown distribution over 252d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(14).rolling(70).mean())
    return _rolling_skew(base, 252)

def tbrk_476_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 33 trend breakdown over 5d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(14).rolling(70).mean())
    return _rolling_kurt(base, 5)

def tbrk_477_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 33 trend breakdown over 21d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(14).rolling(70).mean())
    return _rolling_kurt(base, 21)

def tbrk_478_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 33 trend breakdown over 63d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(14).rolling(70).mean())
    return _rolling_kurt(base, 63)

def tbrk_479_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 33 trend breakdown over 126d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(14).rolling(70).mean())
    return _rolling_kurt(base, 126)

def tbrk_480_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 33 trend breakdown over 252d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(14).rolling(70).mean())
    return _rolling_kurt(base, 252)

def tbrk_481_voladj_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 33 trend breakdown for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(14).rolling(70).mean())
    return _safe_div(base, _rolling_std(base, 5))

def tbrk_482_voladj_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 33 trend breakdown for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(14).rolling(70).mean())
    return _safe_div(base, _rolling_std(base, 21))

def tbrk_483_voladj_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 33 trend breakdown for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(14).rolling(70).mean())
    return _safe_div(base, _rolling_std(base, 63))

def tbrk_484_voladj_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 33 trend breakdown for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(14).rolling(70).mean())
    return _safe_div(base, _rolling_std(base, 126))

def tbrk_485_voladj_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 33 trend breakdown for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(14).rolling(70).mean())
    return _safe_div(base, _rolling_std(base, 252))

def tbrk_486_lognorm_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 33 trend breakdown over 5d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(14).rolling(70).mean())
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def tbrk_487_lognorm_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 33 trend breakdown over 21d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(14).rolling(70).mean())
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def tbrk_488_lognorm_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 33 trend breakdown over 63d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(14).rolling(70).mean())
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def tbrk_489_lognorm_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 33 trend breakdown over 126d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(14).rolling(70).mean())
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def tbrk_490_lognorm_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 33 trend breakdown over 252d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(14).rolling(70).mean())
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def tbrk_491_lvl_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 33 trend breakdown over a 5d horizon to identify extreme regimes.
    """
    base = (close.pct_change(15).rolling(75).mean())
    return _rolling_mean(base, 5)

def tbrk_492_lvl_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 33 trend breakdown over a 21d horizon to identify extreme regimes.
    """
    base = (close.pct_change(15).rolling(75).mean())
    return _rolling_mean(base, 21)

def tbrk_493_lvl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 33 trend breakdown over a 63d horizon to identify extreme regimes.
    """
    base = (close.pct_change(15).rolling(75).mean())
    return _rolling_mean(base, 63)

def tbrk_494_lvl_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 33 trend breakdown over a 126d horizon to identify extreme regimes.
    """
    base = (close.pct_change(15).rolling(75).mean())
    return _rolling_mean(base, 126)

def tbrk_495_lvl_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 33 trend breakdown over a 252d horizon to identify extreme regimes.
    """
    base = (close.pct_change(15).rolling(75).mean())
    return _rolling_mean(base, 252)

def tbrk_496_zscore_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 33 trend breakdown by measuring deviations from the 5d mean.
    """
    base = (close.pct_change(15).rolling(75).mean())
    return _zscore_rolling(base, 5)

def tbrk_497_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 33 trend breakdown by measuring deviations from the 21d mean.
    """
    base = (close.pct_change(15).rolling(75).mean())
    return _zscore_rolling(base, 21)

def tbrk_498_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 33 trend breakdown by measuring deviations from the 63d mean.
    """
    base = (close.pct_change(15).rolling(75).mean())
    return _zscore_rolling(base, 63)

def tbrk_499_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 33 trend breakdown by measuring deviations from the 126d mean.
    """
    base = (close.pct_change(15).rolling(75).mean())
    return _zscore_rolling(base, 126)

def tbrk_500_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 33 trend breakdown by measuring deviations from the 252d mean.
    """
    base = (close.pct_change(15).rolling(75).mean())
    return _zscore_rolling(base, 252)

def tbrk_501_rank_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 33 trend breakdown to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = (close.pct_change(15).rolling(75).mean())
    return _rank_pct(base, 5)

def tbrk_502_rank_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 33 trend breakdown to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = (close.pct_change(15).rolling(75).mean())
    return _rank_pct(base, 21)

def tbrk_503_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 33 trend breakdown to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = (close.pct_change(15).rolling(75).mean())
    return _rank_pct(base, 63)

def tbrk_504_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 33 trend breakdown to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = (close.pct_change(15).rolling(75).mean())
    return _rank_pct(base, 126)

def tbrk_505_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 33 trend breakdown to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = (close.pct_change(15).rolling(75).mean())
    return _rank_pct(base, 252)

def tbrk_506_skew_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 33 trend breakdown distribution over 5d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(15).rolling(75).mean())
    return _rolling_skew(base, 5)

def tbrk_507_skew_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 33 trend breakdown distribution over 21d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(15).rolling(75).mean())
    return _rolling_skew(base, 21)

def tbrk_508_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 33 trend breakdown distribution over 63d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(15).rolling(75).mean())
    return _rolling_skew(base, 63)

def tbrk_509_skew_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 33 trend breakdown distribution over 126d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(15).rolling(75).mean())
    return _rolling_skew(base, 126)

def tbrk_510_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 33 trend breakdown distribution over 252d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(15).rolling(75).mean())
    return _rolling_skew(base, 252)

def tbrk_511_kurt_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 33 trend breakdown over 5d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(15).rolling(75).mean())
    return _rolling_kurt(base, 5)

def tbrk_512_kurt_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 33 trend breakdown over 21d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(15).rolling(75).mean())
    return _rolling_kurt(base, 21)

def tbrk_513_kurt_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 33 trend breakdown over 63d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(15).rolling(75).mean())
    return _rolling_kurt(base, 63)

def tbrk_514_kurt_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 33 trend breakdown over 126d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(15).rolling(75).mean())
    return _rolling_kurt(base, 126)

def tbrk_515_kurt_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 33 trend breakdown over 252d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(15).rolling(75).mean())
    return _rolling_kurt(base, 252)

def tbrk_516_voladj_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 33 trend breakdown for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(15).rolling(75).mean())
    return _safe_div(base, _rolling_std(base, 5))

def tbrk_517_voladj_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 33 trend breakdown for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(15).rolling(75).mean())
    return _safe_div(base, _rolling_std(base, 21))

def tbrk_518_voladj_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 33 trend breakdown for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(15).rolling(75).mean())
    return _safe_div(base, _rolling_std(base, 63))

def tbrk_519_voladj_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 33 trend breakdown for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(15).rolling(75).mean())
    return _safe_div(base, _rolling_std(base, 126))

def tbrk_520_voladj_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 33 trend breakdown for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(15).rolling(75).mean())
    return _safe_div(base, _rolling_std(base, 252))

def tbrk_521_lognorm_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 33 trend breakdown over 5d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(15).rolling(75).mean())
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def tbrk_522_lognorm_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 33 trend breakdown over 21d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(15).rolling(75).mean())
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def tbrk_523_lognorm_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 33 trend breakdown over 63d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(15).rolling(75).mean())
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def tbrk_524_lognorm_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 33 trend breakdown over 126d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(15).rolling(75).mean())
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def tbrk_525_lognorm_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 33 trend breakdown over 252d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(15).rolling(75).mean())
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))
