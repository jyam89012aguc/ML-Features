"""
58_58_trading_intensity — Base Features 451-525
Domain: 58_trading_intensity
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

def tint_451_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 58 trading intensity over 5d to stabilize variance and capture exponential shifts.
    """
    base = (volume.pct_change(13).rolling(65).mean())
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def tint_452_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 58 trading intensity over 21d to stabilize variance and capture exponential shifts.
    """
    base = (volume.pct_change(13).rolling(65).mean())
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def tint_453_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 58 trading intensity over 63d to stabilize variance and capture exponential shifts.
    """
    base = (volume.pct_change(13).rolling(65).mean())
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def tint_454_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 58 trading intensity over 126d to stabilize variance and capture exponential shifts.
    """
    base = (volume.pct_change(13).rolling(65).mean())
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def tint_455_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 58 trading intensity over 252d to stabilize variance and capture exponential shifts.
    """
    base = (volume.pct_change(13).rolling(65).mean())
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def tint_456_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 58 trading intensity over a 5d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(14).rolling(70).mean())
    return _rolling_mean(base, 5)

def tint_457_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 58 trading intensity over a 21d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(14).rolling(70).mean())
    return _rolling_mean(base, 21)

def tint_458_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 58 trading intensity over a 63d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(14).rolling(70).mean())
    return _rolling_mean(base, 63)

def tint_459_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 58 trading intensity over a 126d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(14).rolling(70).mean())
    return _rolling_mean(base, 126)

def tint_460_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 58 trading intensity over a 252d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(14).rolling(70).mean())
    return _rolling_mean(base, 252)

def tint_461_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 58 trading intensity by measuring deviations from the 5d mean.
    """
    base = (volume.pct_change(14).rolling(70).mean())
    return _zscore_rolling(base, 5)

def tint_462_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 58 trading intensity by measuring deviations from the 21d mean.
    """
    base = (volume.pct_change(14).rolling(70).mean())
    return _zscore_rolling(base, 21)

def tint_463_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 58 trading intensity by measuring deviations from the 63d mean.
    """
    base = (volume.pct_change(14).rolling(70).mean())
    return _zscore_rolling(base, 63)

def tint_464_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 58 trading intensity by measuring deviations from the 126d mean.
    """
    base = (volume.pct_change(14).rolling(70).mean())
    return _zscore_rolling(base, 126)

def tint_465_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 58 trading intensity by measuring deviations from the 252d mean.
    """
    base = (volume.pct_change(14).rolling(70).mean())
    return _zscore_rolling(base, 252)

def tint_466_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 58 trading intensity to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = (volume.pct_change(14).rolling(70).mean())
    return _rank_pct(base, 5)

def tint_467_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 58 trading intensity to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = (volume.pct_change(14).rolling(70).mean())
    return _rank_pct(base, 21)

def tint_468_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 58 trading intensity to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = (volume.pct_change(14).rolling(70).mean())
    return _rank_pct(base, 63)

def tint_469_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 58 trading intensity to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = (volume.pct_change(14).rolling(70).mean())
    return _rank_pct(base, 126)

def tint_470_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 58 trading intensity to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = (volume.pct_change(14).rolling(70).mean())
    return _rank_pct(base, 252)

def tint_471_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 58 trading intensity distribution over 5d to detect tail risk or exhaustion.
    """
    base = (volume.pct_change(14).rolling(70).mean())
    return _rolling_skew(base, 5)

def tint_472_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 58 trading intensity distribution over 21d to detect tail risk or exhaustion.
    """
    base = (volume.pct_change(14).rolling(70).mean())
    return _rolling_skew(base, 21)

def tint_473_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 58 trading intensity distribution over 63d to detect tail risk or exhaustion.
    """
    base = (volume.pct_change(14).rolling(70).mean())
    return _rolling_skew(base, 63)

def tint_474_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 58 trading intensity distribution over 126d to detect tail risk or exhaustion.
    """
    base = (volume.pct_change(14).rolling(70).mean())
    return _rolling_skew(base, 126)

def tint_475_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 58 trading intensity distribution over 252d to detect tail risk or exhaustion.
    """
    base = (volume.pct_change(14).rolling(70).mean())
    return _rolling_skew(base, 252)

def tint_476_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 58 trading intensity over 5d to capture explosive breakdown or reversal points.
    """
    base = (volume.pct_change(14).rolling(70).mean())
    return _rolling_kurt(base, 5)

def tint_477_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 58 trading intensity over 21d to capture explosive breakdown or reversal points.
    """
    base = (volume.pct_change(14).rolling(70).mean())
    return _rolling_kurt(base, 21)

def tint_478_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 58 trading intensity over 63d to capture explosive breakdown or reversal points.
    """
    base = (volume.pct_change(14).rolling(70).mean())
    return _rolling_kurt(base, 63)

def tint_479_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 58 trading intensity over 126d to capture explosive breakdown or reversal points.
    """
    base = (volume.pct_change(14).rolling(70).mean())
    return _rolling_kurt(base, 126)

def tint_480_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 58 trading intensity over 252d to capture explosive breakdown or reversal points.
    """
    base = (volume.pct_change(14).rolling(70).mean())
    return _rolling_kurt(base, 252)

def tint_481_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 58 trading intensity for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = (volume.pct_change(14).rolling(70).mean())
    return _safe_div(base, _rolling_std(base, 5))

def tint_482_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 58 trading intensity for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = (volume.pct_change(14).rolling(70).mean())
    return _safe_div(base, _rolling_std(base, 21))

def tint_483_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 58 trading intensity for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = (volume.pct_change(14).rolling(70).mean())
    return _safe_div(base, _rolling_std(base, 63))

def tint_484_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 58 trading intensity for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = (volume.pct_change(14).rolling(70).mean())
    return _safe_div(base, _rolling_std(base, 126))

def tint_485_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 58 trading intensity for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = (volume.pct_change(14).rolling(70).mean())
    return _safe_div(base, _rolling_std(base, 252))

def tint_486_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 58 trading intensity over 5d to stabilize variance and capture exponential shifts.
    """
    base = (volume.pct_change(14).rolling(70).mean())
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def tint_487_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 58 trading intensity over 21d to stabilize variance and capture exponential shifts.
    """
    base = (volume.pct_change(14).rolling(70).mean())
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def tint_488_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 58 trading intensity over 63d to stabilize variance and capture exponential shifts.
    """
    base = (volume.pct_change(14).rolling(70).mean())
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def tint_489_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 58 trading intensity over 126d to stabilize variance and capture exponential shifts.
    """
    base = (volume.pct_change(14).rolling(70).mean())
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def tint_490_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 58 trading intensity over 252d to stabilize variance and capture exponential shifts.
    """
    base = (volume.pct_change(14).rolling(70).mean())
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def tint_491_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 58 trading intensity over a 5d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(15).rolling(75).mean())
    return _rolling_mean(base, 5)

def tint_492_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 58 trading intensity over a 21d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(15).rolling(75).mean())
    return _rolling_mean(base, 21)

def tint_493_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 58 trading intensity over a 63d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(15).rolling(75).mean())
    return _rolling_mean(base, 63)

def tint_494_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 58 trading intensity over a 126d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(15).rolling(75).mean())
    return _rolling_mean(base, 126)

def tint_495_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 58 trading intensity over a 252d horizon to identify extreme regimes.
    """
    base = (volume.pct_change(15).rolling(75).mean())
    return _rolling_mean(base, 252)

def tint_496_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 58 trading intensity by measuring deviations from the 5d mean.
    """
    base = (volume.pct_change(15).rolling(75).mean())
    return _zscore_rolling(base, 5)

def tint_497_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 58 trading intensity by measuring deviations from the 21d mean.
    """
    base = (volume.pct_change(15).rolling(75).mean())
    return _zscore_rolling(base, 21)

def tint_498_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 58 trading intensity by measuring deviations from the 63d mean.
    """
    base = (volume.pct_change(15).rolling(75).mean())
    return _zscore_rolling(base, 63)

def tint_499_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 58 trading intensity by measuring deviations from the 126d mean.
    """
    base = (volume.pct_change(15).rolling(75).mean())
    return _zscore_rolling(base, 126)

def tint_500_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 58 trading intensity by measuring deviations from the 252d mean.
    """
    base = (volume.pct_change(15).rolling(75).mean())
    return _zscore_rolling(base, 252)

def tint_501_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 58 trading intensity to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = (volume.pct_change(15).rolling(75).mean())
    return _rank_pct(base, 5)

def tint_502_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 58 trading intensity to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = (volume.pct_change(15).rolling(75).mean())
    return _rank_pct(base, 21)

def tint_503_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 58 trading intensity to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = (volume.pct_change(15).rolling(75).mean())
    return _rank_pct(base, 63)

def tint_504_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 58 trading intensity to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = (volume.pct_change(15).rolling(75).mean())
    return _rank_pct(base, 126)

def tint_505_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 58 trading intensity to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = (volume.pct_change(15).rolling(75).mean())
    return _rank_pct(base, 252)

def tint_506_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 58 trading intensity distribution over 5d to detect tail risk or exhaustion.
    """
    base = (volume.pct_change(15).rolling(75).mean())
    return _rolling_skew(base, 5)

def tint_507_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 58 trading intensity distribution over 21d to detect tail risk or exhaustion.
    """
    base = (volume.pct_change(15).rolling(75).mean())
    return _rolling_skew(base, 21)

def tint_508_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 58 trading intensity distribution over 63d to detect tail risk or exhaustion.
    """
    base = (volume.pct_change(15).rolling(75).mean())
    return _rolling_skew(base, 63)

def tint_509_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 58 trading intensity distribution over 126d to detect tail risk or exhaustion.
    """
    base = (volume.pct_change(15).rolling(75).mean())
    return _rolling_skew(base, 126)

def tint_510_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 58 trading intensity distribution over 252d to detect tail risk or exhaustion.
    """
    base = (volume.pct_change(15).rolling(75).mean())
    return _rolling_skew(base, 252)

def tint_511_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 58 trading intensity over 5d to capture explosive breakdown or reversal points.
    """
    base = (volume.pct_change(15).rolling(75).mean())
    return _rolling_kurt(base, 5)

def tint_512_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 58 trading intensity over 21d to capture explosive breakdown or reversal points.
    """
    base = (volume.pct_change(15).rolling(75).mean())
    return _rolling_kurt(base, 21)

def tint_513_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 58 trading intensity over 63d to capture explosive breakdown or reversal points.
    """
    base = (volume.pct_change(15).rolling(75).mean())
    return _rolling_kurt(base, 63)

def tint_514_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 58 trading intensity over 126d to capture explosive breakdown or reversal points.
    """
    base = (volume.pct_change(15).rolling(75).mean())
    return _rolling_kurt(base, 126)

def tint_515_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 58 trading intensity over 252d to capture explosive breakdown or reversal points.
    """
    base = (volume.pct_change(15).rolling(75).mean())
    return _rolling_kurt(base, 252)

def tint_516_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 58 trading intensity for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = (volume.pct_change(15).rolling(75).mean())
    return _safe_div(base, _rolling_std(base, 5))

def tint_517_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 58 trading intensity for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = (volume.pct_change(15).rolling(75).mean())
    return _safe_div(base, _rolling_std(base, 21))

def tint_518_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 58 trading intensity for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = (volume.pct_change(15).rolling(75).mean())
    return _safe_div(base, _rolling_std(base, 63))

def tint_519_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 58 trading intensity for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = (volume.pct_change(15).rolling(75).mean())
    return _safe_div(base, _rolling_std(base, 126))

def tint_520_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 58 trading intensity for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = (volume.pct_change(15).rolling(75).mean())
    return _safe_div(base, _rolling_std(base, 252))

def tint_521_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 58 trading intensity over 5d to stabilize variance and capture exponential shifts.
    """
    base = (volume.pct_change(15).rolling(75).mean())
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def tint_522_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 58 trading intensity over 21d to stabilize variance and capture exponential shifts.
    """
    base = (volume.pct_change(15).rolling(75).mean())
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def tint_523_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 58 trading intensity over 63d to stabilize variance and capture exponential shifts.
    """
    base = (volume.pct_change(15).rolling(75).mean())
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def tint_524_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 58 trading intensity over 126d to stabilize variance and capture exponential shifts.
    """
    base = (volume.pct_change(15).rolling(75).mean())
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def tint_525_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 58 trading intensity over 252d to stabilize variance and capture exponential shifts.
    """
    base = (volume.pct_change(15).rolling(75).mean())
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))
