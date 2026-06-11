"""
41_41_range_compression — Base Features 451-525
Domain: 41_range_compression
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

def rcmp_451_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 41 range compression over 5d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(13).rolling(65).mean())
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def rcmp_452_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 41 range compression over 21d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(13).rolling(65).mean())
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def rcmp_453_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 41 range compression over 63d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(13).rolling(65).mean())
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def rcmp_454_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 41 range compression over 126d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(13).rolling(65).mean())
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def rcmp_455_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 41 range compression over 252d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(13).rolling(65).mean())
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def rcmp_456_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 41 range compression over a 5d horizon to identify extreme regimes.
    """
    base = (close.pct_change(14).rolling(70).mean())
    return _rolling_mean(base, 5)

def rcmp_457_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 41 range compression over a 21d horizon to identify extreme regimes.
    """
    base = (close.pct_change(14).rolling(70).mean())
    return _rolling_mean(base, 21)

def rcmp_458_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 41 range compression over a 63d horizon to identify extreme regimes.
    """
    base = (close.pct_change(14).rolling(70).mean())
    return _rolling_mean(base, 63)

def rcmp_459_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 41 range compression over a 126d horizon to identify extreme regimes.
    """
    base = (close.pct_change(14).rolling(70).mean())
    return _rolling_mean(base, 126)

def rcmp_460_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 41 range compression over a 252d horizon to identify extreme regimes.
    """
    base = (close.pct_change(14).rolling(70).mean())
    return _rolling_mean(base, 252)

def rcmp_461_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 41 range compression by measuring deviations from the 5d mean.
    """
    base = (close.pct_change(14).rolling(70).mean())
    return _zscore_rolling(base, 5)

def rcmp_462_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 41 range compression by measuring deviations from the 21d mean.
    """
    base = (close.pct_change(14).rolling(70).mean())
    return _zscore_rolling(base, 21)

def rcmp_463_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 41 range compression by measuring deviations from the 63d mean.
    """
    base = (close.pct_change(14).rolling(70).mean())
    return _zscore_rolling(base, 63)

def rcmp_464_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 41 range compression by measuring deviations from the 126d mean.
    """
    base = (close.pct_change(14).rolling(70).mean())
    return _zscore_rolling(base, 126)

def rcmp_465_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 41 range compression by measuring deviations from the 252d mean.
    """
    base = (close.pct_change(14).rolling(70).mean())
    return _zscore_rolling(base, 252)

def rcmp_466_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 41 range compression to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = (close.pct_change(14).rolling(70).mean())
    return _rank_pct(base, 5)

def rcmp_467_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 41 range compression to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = (close.pct_change(14).rolling(70).mean())
    return _rank_pct(base, 21)

def rcmp_468_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 41 range compression to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = (close.pct_change(14).rolling(70).mean())
    return _rank_pct(base, 63)

def rcmp_469_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 41 range compression to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = (close.pct_change(14).rolling(70).mean())
    return _rank_pct(base, 126)

def rcmp_470_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 41 range compression to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = (close.pct_change(14).rolling(70).mean())
    return _rank_pct(base, 252)

def rcmp_471_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 41 range compression distribution over 5d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(14).rolling(70).mean())
    return _rolling_skew(base, 5)

def rcmp_472_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 41 range compression distribution over 21d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(14).rolling(70).mean())
    return _rolling_skew(base, 21)

def rcmp_473_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 41 range compression distribution over 63d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(14).rolling(70).mean())
    return _rolling_skew(base, 63)

def rcmp_474_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 41 range compression distribution over 126d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(14).rolling(70).mean())
    return _rolling_skew(base, 126)

def rcmp_475_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 41 range compression distribution over 252d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(14).rolling(70).mean())
    return _rolling_skew(base, 252)

def rcmp_476_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 41 range compression over 5d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(14).rolling(70).mean())
    return _rolling_kurt(base, 5)

def rcmp_477_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 41 range compression over 21d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(14).rolling(70).mean())
    return _rolling_kurt(base, 21)

def rcmp_478_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 41 range compression over 63d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(14).rolling(70).mean())
    return _rolling_kurt(base, 63)

def rcmp_479_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 41 range compression over 126d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(14).rolling(70).mean())
    return _rolling_kurt(base, 126)

def rcmp_480_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 41 range compression over 252d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(14).rolling(70).mean())
    return _rolling_kurt(base, 252)

def rcmp_481_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 41 range compression for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(14).rolling(70).mean())
    return _safe_div(base, _rolling_std(base, 5))

def rcmp_482_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 41 range compression for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(14).rolling(70).mean())
    return _safe_div(base, _rolling_std(base, 21))

def rcmp_483_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 41 range compression for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(14).rolling(70).mean())
    return _safe_div(base, _rolling_std(base, 63))

def rcmp_484_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 41 range compression for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(14).rolling(70).mean())
    return _safe_div(base, _rolling_std(base, 126))

def rcmp_485_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 41 range compression for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(14).rolling(70).mean())
    return _safe_div(base, _rolling_std(base, 252))

def rcmp_486_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 41 range compression over 5d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(14).rolling(70).mean())
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def rcmp_487_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 41 range compression over 21d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(14).rolling(70).mean())
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def rcmp_488_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 41 range compression over 63d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(14).rolling(70).mean())
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def rcmp_489_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 41 range compression over 126d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(14).rolling(70).mean())
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def rcmp_490_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 41 range compression over 252d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(14).rolling(70).mean())
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))

def rcmp_491_lvl_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 41 range compression over a 5d horizon to identify extreme regimes.
    """
    base = (close.pct_change(15).rolling(75).mean())
    return _rolling_mean(base, 5)

def rcmp_492_lvl_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 41 range compression over a 21d horizon to identify extreme regimes.
    """
    base = (close.pct_change(15).rolling(75).mean())
    return _rolling_mean(base, 21)

def rcmp_493_lvl_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 41 range compression over a 63d horizon to identify extreme regimes.
    """
    base = (close.pct_change(15).rolling(75).mean())
    return _rolling_mean(base, 63)

def rcmp_494_lvl_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 41 range compression over a 126d horizon to identify extreme regimes.
    """
    base = (close.pct_change(15).rolling(75).mean())
    return _rolling_mean(base, 126)

def rcmp_495_lvl_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Capture the raw intensity of 41 range compression over a 252d horizon to identify extreme regimes.
    """
    base = (close.pct_change(15).rolling(75).mean())
    return _rolling_mean(base, 252)

def rcmp_496_zscore_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 41 range compression by measuring deviations from the 5d mean.
    """
    base = (close.pct_change(15).rolling(75).mean())
    return _zscore_rolling(base, 5)

def rcmp_497_zscore_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 41 range compression by measuring deviations from the 21d mean.
    """
    base = (close.pct_change(15).rolling(75).mean())
    return _zscore_rolling(base, 21)

def rcmp_498_zscore_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 41 range compression by measuring deviations from the 63d mean.
    """
    base = (close.pct_change(15).rolling(75).mean())
    return _zscore_rolling(base, 63)

def rcmp_499_zscore_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 41 range compression by measuring deviations from the 126d mean.
    """
    base = (close.pct_change(15).rolling(75).mean())
    return _zscore_rolling(base, 126)

def rcmp_500_zscore_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify statistical anomalies in 41 range compression by measuring deviations from the 252d mean.
    """
    base = (close.pct_change(15).rolling(75).mean())
    return _zscore_rolling(base, 252)

def rcmp_501_rank_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 41 range compression to a 0-1 range using a 5d rolling window to assess relative positioning.
    """
    base = (close.pct_change(15).rolling(75).mean())
    return _rank_pct(base, 5)

def rcmp_502_rank_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 41 range compression to a 0-1 range using a 21d rolling window to assess relative positioning.
    """
    base = (close.pct_change(15).rolling(75).mean())
    return _rank_pct(base, 21)

def rcmp_503_rank_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 41 range compression to a 0-1 range using a 63d rolling window to assess relative positioning.
    """
    base = (close.pct_change(15).rolling(75).mean())
    return _rank_pct(base, 63)

def rcmp_504_rank_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 41 range compression to a 0-1 range using a 126d rolling window to assess relative positioning.
    """
    base = (close.pct_change(15).rolling(75).mean())
    return _rank_pct(base, 126)

def rcmp_505_rank_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Normalize 41 range compression to a 0-1 range using a 252d rolling window to assess relative positioning.
    """
    base = (close.pct_change(15).rolling(75).mean())
    return _rank_pct(base, 252)

def rcmp_506_skew_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 41 range compression distribution over 5d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(15).rolling(75).mean())
    return _rolling_skew(base, 5)

def rcmp_507_skew_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 41 range compression distribution over 21d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(15).rolling(75).mean())
    return _rolling_skew(base, 21)

def rcmp_508_skew_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 41 range compression distribution over 63d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(15).rolling(75).mean())
    return _rolling_skew(base, 63)

def rcmp_509_skew_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 41 range compression distribution over 126d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(15).rolling(75).mean())
    return _rolling_skew(base, 126)

def rcmp_510_skew_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Measure the asymmetry of 41 range compression distribution over 252d to detect tail risk or exhaustion.
    """
    base = (close.pct_change(15).rolling(75).mean())
    return _rolling_skew(base, 252)

def rcmp_511_kurt_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 41 range compression over 5d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(15).rolling(75).mean())
    return _rolling_kurt(base, 5)

def rcmp_512_kurt_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 41 range compression over 21d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(15).rolling(75).mean())
    return _rolling_kurt(base, 21)

def rcmp_513_kurt_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 41 range compression over 63d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(15).rolling(75).mean())
    return _rolling_kurt(base, 63)

def rcmp_514_kurt_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 41 range compression over 126d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(15).rolling(75).mean())
    return _rolling_kurt(base, 126)

def rcmp_515_kurt_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Identify fat-tail events in 41 range compression over 252d to capture explosive breakdown or reversal points.
    """
    base = (close.pct_change(15).rolling(75).mean())
    return _rolling_kurt(base, 252)

def rcmp_516_voladj_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 41 range compression for rolling 5d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(15).rolling(75).mean())
    return _safe_div(base, _rolling_std(base, 5))

def rcmp_517_voladj_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 41 range compression for rolling 21d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(15).rolling(75).mean())
    return _safe_div(base, _rolling_std(base, 21))

def rcmp_518_voladj_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 41 range compression for rolling 63d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(15).rolling(75).mean())
    return _safe_div(base, _rolling_std(base, 63))

def rcmp_519_voladj_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 41 range compression for rolling 126d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(15).rolling(75).mean())
    return _safe_div(base, _rolling_std(base, 126))

def rcmp_520_voladj_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Adjust 41 range compression for rolling 252d volatility to filter out noise in high-volatility environments.
    """
    base = (close.pct_change(15).rolling(75).mean())
    return _safe_div(base, _rolling_std(base, 252))

def rcmp_521_lognorm_5d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 41 range compression over 5d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(15).rolling(75).mean())
    return np.log(_rolling_mean(base, 5).clip(lower=_EPS))

def rcmp_522_lognorm_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 41 range compression over 21d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(15).rolling(75).mean())
    return np.log(_rolling_mean(base, 21).clip(lower=_EPS))

def rcmp_523_lognorm_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 41 range compression over 63d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(15).rolling(75).mean())
    return np.log(_rolling_mean(base, 63).clip(lower=_EPS))

def rcmp_524_lognorm_126d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 41 range compression over 126d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(15).rolling(75).mean())
    return np.log(_rolling_mean(base, 126).clip(lower=_EPS))

def rcmp_525_lognorm_252d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Economic Rationale: Apply log-normalization to 41 range compression over 252d to stabilize variance and capture exponential shifts.
    """
    base = (close.pct_change(15).rolling(75).mean())
    return np.log(_rolling_mean(base, 252).clip(lower=_EPS))
