"""
52_52_bar_morphology — Base Features 451-525
Domain: 52_bar_morphology
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

def bmor_451_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 52 bar morphology over 5d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(65).mean())
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def bmor_452_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 52 bar morphology over 21d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(65).mean())
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def bmor_453_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 52 bar morphology over 63d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(65).mean())
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def bmor_454_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 52 bar morphology over 126d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(65).mean())
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def bmor_455_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 52 bar morphology over 252d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(65).mean())
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def bmor_456_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 52 bar morphology over a 5d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(70).mean())
    return _rolling_mean(base, 5)

def bmor_457_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 52 bar morphology over a 21d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(70).mean())
    return _rolling_mean(base, 21)

def bmor_458_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 52 bar morphology over a 63d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(70).mean())
    return _rolling_mean(base, 63)

def bmor_459_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 52 bar morphology over a 126d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(70).mean())
    return _rolling_mean(base, 126)

def bmor_460_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 52 bar morphology over a 252d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(70).mean())
    return _rolling_mean(base, 252)

def bmor_461_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 52 bar morphology by measuring deviations from the 5d mean.
    """
    base = ((close - open).abs().rolling(70).mean())
    return _zscore_rolling(base, 5)

def bmor_462_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 52 bar morphology by measuring deviations from the 21d mean.
    """
    base = ((close - open).abs().rolling(70).mean())
    return _zscore_rolling(base, 21)

def bmor_463_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 52 bar morphology by measuring deviations from the 63d mean.
    """
    base = ((close - open).abs().rolling(70).mean())
    return _zscore_rolling(base, 63)

def bmor_464_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 52 bar morphology by measuring deviations from the 126d mean.
    """
    base = ((close - open).abs().rolling(70).mean())
    return _zscore_rolling(base, 126)

def bmor_465_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 52 bar morphology by measuring deviations from the 252d mean.
    """
    base = ((close - open).abs().rolling(70).mean())
    return _zscore_rolling(base, 252)

def bmor_466_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 52 bar morphology to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(70).mean())
    return _rank_pct(base, 5)

def bmor_467_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 52 bar morphology to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(70).mean())
    return _rank_pct(base, 21)

def bmor_468_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 52 bar morphology to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(70).mean())
    return _rank_pct(base, 63)

def bmor_469_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 52 bar morphology to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(70).mean())
    return _rank_pct(base, 126)

def bmor_470_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 52 bar morphology to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(70).mean())
    return _rank_pct(base, 252)

def bmor_471_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 52 bar morphology distribution over 5d to detect tail risk or exhaustion.
    """
    base = ((close - open).abs().rolling(70).mean())
    return _rolling_skew(base, 5)

def bmor_472_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 52 bar morphology distribution over 21d to detect tail risk or exhaustion.
    """
    base = ((close - open).abs().rolling(70).mean())
    return _rolling_skew(base, 21)

def bmor_473_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 52 bar morphology distribution over 63d to detect tail risk or exhaustion.
    """
    base = ((close - open).abs().rolling(70).mean())
    return _rolling_skew(base, 63)

def bmor_474_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 52 bar morphology distribution over 126d to detect tail risk or exhaustion.
    """
    base = ((close - open).abs().rolling(70).mean())
    return _rolling_skew(base, 126)

def bmor_475_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 52 bar morphology distribution over 252d to detect tail risk or exhaustion.
    """
    base = ((close - open).abs().rolling(70).mean())
    return _rolling_skew(base, 252)

def bmor_476_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 52 bar morphology over 5d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(70).mean())
    return _rolling_kurt(base, 5)

def bmor_477_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 52 bar morphology over 21d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(70).mean())
    return _rolling_kurt(base, 21)

def bmor_478_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 52 bar morphology over 63d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(70).mean())
    return _rolling_kurt(base, 63)

def bmor_479_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 52 bar morphology over 126d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(70).mean())
    return _rolling_kurt(base, 126)

def bmor_480_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 52 bar morphology over 252d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(70).mean())
    return _rolling_kurt(base, 252)

def bmor_481_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 52 bar morphology for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = ((close - open).abs().rolling(70).mean())
    return _safe_div(base, _rolling_std(base, 5))

def bmor_482_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 52 bar morphology for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = ((close - open).abs().rolling(70).mean())
    return _safe_div(base, _rolling_std(base, 21))

def bmor_483_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 52 bar morphology for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = ((close - open).abs().rolling(70).mean())
    return _safe_div(base, _rolling_std(base, 63))

def bmor_484_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 52 bar morphology for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = ((close - open).abs().rolling(70).mean())
    return _safe_div(base, _rolling_std(base, 126))

def bmor_485_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 52 bar morphology for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = ((close - open).abs().rolling(70).mean())
    return _safe_div(base, _rolling_std(base, 252))

def bmor_486_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 52 bar morphology over 5d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(70).mean())
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def bmor_487_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 52 bar morphology over 21d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(70).mean())
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def bmor_488_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 52 bar morphology over 63d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(70).mean())
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def bmor_489_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 52 bar morphology over 126d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(70).mean())
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def bmor_490_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 52 bar morphology over 252d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(70).mean())
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def bmor_491_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 52 bar morphology over a 5d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(75).mean())
    return _rolling_mean(base, 5)

def bmor_492_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 52 bar morphology over a 21d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(75).mean())
    return _rolling_mean(base, 21)

def bmor_493_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 52 bar morphology over a 63d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(75).mean())
    return _rolling_mean(base, 63)

def bmor_494_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 52 bar morphology over a 126d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(75).mean())
    return _rolling_mean(base, 126)

def bmor_495_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 52 bar morphology over a 252d horizon to identify extreme regimes.
    """
    base = ((close - open).abs().rolling(75).mean())
    return _rolling_mean(base, 252)

def bmor_496_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 52 bar morphology by measuring deviations from the 5d mean.
    """
    base = ((close - open).abs().rolling(75).mean())
    return _zscore_rolling(base, 5)

def bmor_497_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 52 bar morphology by measuring deviations from the 21d mean.
    """
    base = ((close - open).abs().rolling(75).mean())
    return _zscore_rolling(base, 21)

def bmor_498_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 52 bar morphology by measuring deviations from the 63d mean.
    """
    base = ((close - open).abs().rolling(75).mean())
    return _zscore_rolling(base, 63)

def bmor_499_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 52 bar morphology by measuring deviations from the 126d mean.
    """
    base = ((close - open).abs().rolling(75).mean())
    return _zscore_rolling(base, 126)

def bmor_500_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 52 bar morphology by measuring deviations from the 252d mean.
    """
    base = ((close - open).abs().rolling(75).mean())
    return _zscore_rolling(base, 252)

def bmor_501_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 52 bar morphology to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(75).mean())
    return _rank_pct(base, 5)

def bmor_502_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 52 bar morphology to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(75).mean())
    return _rank_pct(base, 21)

def bmor_503_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 52 bar morphology to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(75).mean())
    return _rank_pct(base, 63)

def bmor_504_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 52 bar morphology to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(75).mean())
    return _rank_pct(base, 126)

def bmor_505_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 52 bar morphology to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = ((close - open).abs().rolling(75).mean())
    return _rank_pct(base, 252)

def bmor_506_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 52 bar morphology distribution over 5d to detect tail risk or exhaustion.
    """
    base = ((close - open).abs().rolling(75).mean())
    return _rolling_skew(base, 5)

def bmor_507_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 52 bar morphology distribution over 21d to detect tail risk or exhaustion.
    """
    base = ((close - open).abs().rolling(75).mean())
    return _rolling_skew(base, 21)

def bmor_508_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 52 bar morphology distribution over 63d to detect tail risk or exhaustion.
    """
    base = ((close - open).abs().rolling(75).mean())
    return _rolling_skew(base, 63)

def bmor_509_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 52 bar morphology distribution over 126d to detect tail risk or exhaustion.
    """
    base = ((close - open).abs().rolling(75).mean())
    return _rolling_skew(base, 126)

def bmor_510_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 52 bar morphology distribution over 252d to detect tail risk or exhaustion.
    """
    base = ((close - open).abs().rolling(75).mean())
    return _rolling_skew(base, 252)

def bmor_511_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 52 bar morphology over 5d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(75).mean())
    return _rolling_kurt(base, 5)

def bmor_512_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 52 bar morphology over 21d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(75).mean())
    return _rolling_kurt(base, 21)

def bmor_513_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 52 bar morphology over 63d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(75).mean())
    return _rolling_kurt(base, 63)

def bmor_514_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 52 bar morphology over 126d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(75).mean())
    return _rolling_kurt(base, 126)

def bmor_515_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 52 bar morphology over 252d to capture explosive breakdown or reversal points.
    """
    base = ((close - open).abs().rolling(75).mean())
    return _rolling_kurt(base, 252)

def bmor_516_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 52 bar morphology for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = ((close - open).abs().rolling(75).mean())
    return _safe_div(base, _rolling_std(base, 5))

def bmor_517_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 52 bar morphology for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = ((close - open).abs().rolling(75).mean())
    return _safe_div(base, _rolling_std(base, 21))

def bmor_518_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 52 bar morphology for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = ((close - open).abs().rolling(75).mean())
    return _safe_div(base, _rolling_std(base, 63))

def bmor_519_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 52 bar morphology for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = ((close - open).abs().rolling(75).mean())
    return _safe_div(base, _rolling_std(base, 126))

def bmor_520_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 52 bar morphology for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = ((close - open).abs().rolling(75).mean())
    return _safe_div(base, _rolling_std(base, 252))

def bmor_521_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 52 bar morphology over 5d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(75).mean())
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def bmor_522_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 52 bar morphology over 21d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(75).mean())
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def bmor_523_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 52 bar morphology over 63d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(75).mean())
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def bmor_524_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 52 bar morphology over 126d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(75).mean())
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def bmor_525_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 52 bar morphology over 252d to stabilize variance and capture exponential shifts.
    """
    base = ((close - open).abs().rolling(75).mean())
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))
