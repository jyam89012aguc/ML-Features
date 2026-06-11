"""
48_48_open_close_dynamics — Base Features 451-525
Domain: 48_open_close_dynamics
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

def ocdy_451_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 48 open close dynamics over 5d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(65).mean())
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def ocdy_452_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 48 open close dynamics over 21d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(65).mean())
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def ocdy_453_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 48 open close dynamics over 63d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(65).mean())
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def ocdy_454_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 48 open close dynamics over 126d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(65).mean())
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def ocdy_455_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 48 open close dynamics over 252d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(65).mean())
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def ocdy_456_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 48 open close dynamics over a 5d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(70).mean())
    return _rolling_mean(base, 5)

def ocdy_457_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 48 open close dynamics over a 21d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(70).mean())
    return _rolling_mean(base, 21)

def ocdy_458_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 48 open close dynamics over a 63d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(70).mean())
    return _rolling_mean(base, 63)

def ocdy_459_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 48 open close dynamics over a 126d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(70).mean())
    return _rolling_mean(base, 126)

def ocdy_460_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 48 open close dynamics over a 252d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(70).mean())
    return _rolling_mean(base, 252)

def ocdy_461_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 48 open close dynamics by measuring deviations from the 5d mean.
    """
    base = ((close - open).abs().rolling(70).mean())
    return _zscore_rolling(base, 5)

def ocdy_462_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 48 open close dynamics by measuring deviations from the 21d mean.
    """
    base = ((close - open).abs().rolling(70).mean())
    return _zscore_rolling(base, 21)

def ocdy_463_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 48 open close dynamics by measuring deviations from the 63d mean.
    """
    base = ((close - open).abs().rolling(70).mean())
    return _zscore_rolling(base, 63)

def ocdy_464_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 48 open close dynamics by measuring deviations from the 126d mean.
    """
    base = ((close - open).abs().rolling(70).mean())
    return _zscore_rolling(base, 126)

def ocdy_465_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 48 open close dynamics by measuring deviations from the 252d mean.
    """
    base = ((close - open).abs().rolling(70).mean())
    return _zscore_rolling(base, 252)

def ocdy_466_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 48 open close dynamics to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(70).mean())
    return _rank_pct(base, 5)

def ocdy_467_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 48 open close dynamics to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(70).mean())
    return _rank_pct(base, 21)

def ocdy_468_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 48 open close dynamics to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(70).mean())
    return _rank_pct(base, 63)

def ocdy_469_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 48 open close dynamics to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(70).mean())
    return _rank_pct(base, 126)

def ocdy_470_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 48 open close dynamics to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(70).mean())
    return _rank_pct(base, 252)

def ocdy_471_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 48 open close dynamics distribution over 5d to detect tail risk or exhaustion.
    """
    base = ((close - open).abs().rolling(70).mean())
    return _rolling_skew(base, 5)

def ocdy_472_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 48 open close dynamics distribution over 21d to detect tail risk or exhaustion.
    """
    base = ((close - open).abs().rolling(70).mean())
    return _rolling_skew(base, 21)

def ocdy_473_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 48 open close dynamics distribution over 63d to detect tail risk or exhaustion.
    """
    base = ((close - open).abs().rolling(70).mean())
    return _rolling_skew(base, 63)

def ocdy_474_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 48 open close dynamics distribution over 126d to detect tail risk or exhaustion.
    """
    base = ((close - open).abs().rolling(70).mean())
    return _rolling_skew(base, 126)

def ocdy_475_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 48 open close dynamics distribution over 252d to detect tail risk or exhaustion.
    """
    base = ((close - open).abs().rolling(70).mean())
    return _rolling_skew(base, 252)

def ocdy_476_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 48 open close dynamics over 5d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(70).mean())
    return _rolling_kurt(base, 5)

def ocdy_477_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 48 open close dynamics over 21d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(70).mean())
    return _rolling_kurt(base, 21)

def ocdy_478_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 48 open close dynamics over 63d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(70).mean())
    return _rolling_kurt(base, 63)

def ocdy_479_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 48 open close dynamics over 126d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(70).mean())
    return _rolling_kurt(base, 126)

def ocdy_480_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 48 open close dynamics over 252d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(70).mean())
    return _rolling_kurt(base, 252)

def ocdy_481_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 48 open close dynamics for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = ((close - open).abs().rolling(70).mean())
    return _safe_div(base, _rolling_std(base, 5))

def ocdy_482_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 48 open close dynamics for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = ((close - open).abs().rolling(70).mean())
    return _safe_div(base, _rolling_std(base, 21))

def ocdy_483_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 48 open close dynamics for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = ((close - open).abs().rolling(70).mean())
    return _safe_div(base, _rolling_std(base, 63))

def ocdy_484_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 48 open close dynamics for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = ((close - open).abs().rolling(70).mean())
    return _safe_div(base, _rolling_std(base, 126))

def ocdy_485_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 48 open close dynamics for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = ((close - open).abs().rolling(70).mean())
    return _safe_div(base, _rolling_std(base, 252))

def ocdy_486_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 48 open close dynamics over 5d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(70).mean())
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def ocdy_487_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 48 open close dynamics over 21d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(70).mean())
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def ocdy_488_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 48 open close dynamics over 63d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(70).mean())
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def ocdy_489_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 48 open close dynamics over 126d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(70).mean())
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def ocdy_490_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 48 open close dynamics over 252d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(70).mean())
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def ocdy_491_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 48 open close dynamics over a 5d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(75).mean())
    return _rolling_mean(base, 5)

def ocdy_492_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 48 open close dynamics over a 21d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(75).mean())
    return _rolling_mean(base, 21)

def ocdy_493_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 48 open close dynamics over a 63d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(75).mean())
    return _rolling_mean(base, 63)

def ocdy_494_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 48 open close dynamics over a 126d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(75).mean())
    return _rolling_mean(base, 126)

def ocdy_495_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 48 open close dynamics over a 252d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(75).mean())
    return _rolling_mean(base, 252)

def ocdy_496_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 48 open close dynamics by measuring deviations from the 5d mean.
    """
    base = ((close - open).abs().rolling(75).mean())
    return _zscore_rolling(base, 5)

def ocdy_497_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 48 open close dynamics by measuring deviations from the 21d mean.
    """
    base = ((close - open).abs().rolling(75).mean())
    return _zscore_rolling(base, 21)

def ocdy_498_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 48 open close dynamics by measuring deviations from the 63d mean.
    """
    base = ((close - open).abs().rolling(75).mean())
    return _zscore_rolling(base, 63)

def ocdy_499_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 48 open close dynamics by measuring deviations from the 126d mean.
    """
    base = ((close - open).abs().rolling(75).mean())
    return _zscore_rolling(base, 126)

def ocdy_500_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 48 open close dynamics by measuring deviations from the 252d mean.
    """
    base = ((close - open).abs().rolling(75).mean())
    return _zscore_rolling(base, 252)

def ocdy_501_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 48 open close dynamics to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(75).mean())
    return _rank_pct(base, 5)

def ocdy_502_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 48 open close dynamics to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(75).mean())
    return _rank_pct(base, 21)

def ocdy_503_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 48 open close dynamics to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(75).mean())
    return _rank_pct(base, 63)

def ocdy_504_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 48 open close dynamics to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(75).mean())
    return _rank_pct(base, 126)

def ocdy_505_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 48 open close dynamics to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(75).mean())
    return _rank_pct(base, 252)

def ocdy_506_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 48 open close dynamics distribution over 5d to detect tail risk or exhaustion.
    """
    base = ((close - open).abs().rolling(75).mean())
    return _rolling_skew(base, 5)

def ocdy_507_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 48 open close dynamics distribution over 21d to detect tail risk or exhaustion.
    """
    base = ((close - open).abs().rolling(75).mean())
    return _rolling_skew(base, 21)

def ocdy_508_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 48 open close dynamics distribution over 63d to detect tail risk or exhaustion.
    """
    base = ((close - open).abs().rolling(75).mean())
    return _rolling_skew(base, 63)

def ocdy_509_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 48 open close dynamics distribution over 126d to detect tail risk or exhaustion.
    """
    base = ((close - open).abs().rolling(75).mean())
    return _rolling_skew(base, 126)

def ocdy_510_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 48 open close dynamics distribution over 252d to detect tail risk or exhaustion.
    """
    base = ((close - open).abs().rolling(75).mean())
    return _rolling_skew(base, 252)

def ocdy_511_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 48 open close dynamics over 5d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(75).mean())
    return _rolling_kurt(base, 5)

def ocdy_512_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 48 open close dynamics over 21d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(75).mean())
    return _rolling_kurt(base, 21)

def ocdy_513_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 48 open close dynamics over 63d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(75).mean())
    return _rolling_kurt(base, 63)

def ocdy_514_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 48 open close dynamics over 126d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(75).mean())
    return _rolling_kurt(base, 126)

def ocdy_515_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 48 open close dynamics over 252d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(75).mean())
    return _rolling_kurt(base, 252)

def ocdy_516_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 48 open close dynamics for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = ((close - open).abs().rolling(75).mean())
    return _safe_div(base, _rolling_std(base, 5))

def ocdy_517_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 48 open close dynamics for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = ((close - open).abs().rolling(75).mean())
    return _safe_div(base, _rolling_std(base, 21))

def ocdy_518_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 48 open close dynamics for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = ((close - open).abs().rolling(75).mean())
    return _safe_div(base, _rolling_std(base, 63))

def ocdy_519_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 48 open close dynamics for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = ((close - open).abs().rolling(75).mean())
    return _safe_div(base, _rolling_std(base, 126))

def ocdy_520_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 48 open close dynamics for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = ((close - open).abs().rolling(75).mean())
    return _safe_div(base, _rolling_std(base, 252))

def ocdy_521_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 48 open close dynamics over 5d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(75).mean())
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def ocdy_522_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 48 open close dynamics over 21d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(75).mean())
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def ocdy_523_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 48 open close dynamics over 63d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(75).mean())
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def ocdy_524_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 48 open close dynamics over 126d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(75).mean())
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def ocdy_525_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 48 open close dynamics over 252d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(75).mean())
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))
